from django import forms
from django.core.exceptions import ValidationError

from api.models import TeamMember

admin_choices = [(True, 'Regular - Can\'t delete members'),
                 (False, 'Admin - Can delete members')]

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ('first_name', 'last_name',
                  'email', 'phone_number', 'is_admin')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name':  forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}), 
            'is_admin': forms.RadioSelect(choices=admin_choices),
        }
