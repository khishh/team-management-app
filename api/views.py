from django.shortcuts import render
from django.views.generic import ListView, DetailView
from rest_framework import viewsets

from .serializer import TeamMemberSerializer
from .models import TeamMember

# Delete below
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

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

    def onclick():
        print('button clicked')

