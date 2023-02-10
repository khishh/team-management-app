from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from django.http import HttpResponseRedirect

from .serializer import TeamMemberSerializer
from .models import TeamMember
from .forms import TeamMemberForm

# Create your views here.


class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer


class TeamMemberListView(ListView):
    model = TeamMember
    template_name = 'teammembers/teammember_list.html'
    context_object_name = 'team_members'


class TeamMemberDetailView(DetailView):
    model = TeamMember
    template_name = 'teammembers/teammember_details.html'
    context_object_name = 'team_member'


# Form below

def convert_member_from_form(cleaned_data: dict):
    first_name = cleaned_data['first_name']
    last_name = cleaned_data['last_name']
    email = cleaned_data['email']
    phone_number = cleaned_data['phone_number']
    is_admin = cleaned_data['is_admin']
    return TeamMember(first_name=first_name, last_name=last_name,
                      email=email, phone_number=phone_number, is_admin=is_admin)


def add_teammember_form(request):
    if request.method == 'POST':
        form = TeamMemberForm(request.POST)

        if form.is_valid():
            new_member = convert_member_from_form(form.cleaned_data)
            new_member.save()
            return HttpResponseRedirect('/teammembers')

    else:
        form = TeamMemberForm()

    return render(request, 'teammembers/teammember_add_form.html', {'form': form})

def edit_teammember_form(request, pk):
    teammember = get_object_or_404(TeamMember, pk=pk)
    print(teammember.first_name)
    if request.method == 'POST':
        form = TeamMemberForm(request.POST)

        if form.is_valid():
            new_member = convert_member_from_form(form.cleaned_data)
            new_member.save()
            return HttpResponseRedirect('/teammembers')

    else:
        form = TeamMemberForm()

    return render(request, 'teammembers/teammember_add_form.html', {'form': form})
