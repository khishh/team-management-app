from django import forms
from django.core.exceptions import ValidationError

from api.models import TeamMember

admin_choices = [(True, 'Regular - Can\'t delete members'),
                 (False, 'Admin - Can delete members')]


class TeamMemberForm(forms.Form):

    first_name = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=255, widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    phone_number = forms.CharField(
        max_length=12, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_admin = forms.BooleanField(
        required=False, widget=forms.RadioSelect(choices=admin_choices), label='')

# class TeammemberForm(forms.ModelForm):
#     class Meta:
#         model = TeamMember
