from django import forms
from django.core.exceptions import ValidationError

from api.models import TeamMember

admin_choices = [(False, 'Regular - Can\'t delete members'),
                 (True, 'Admin - Can delete members')]

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ('first_name', 'last_name',
                  'email', 'phone_number', 'is_admin')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'input_first_name'}),
            'last_name':  forms.TextInput(attrs={'class': 'form-control', 'id': 'input_last_name'}, ),
            'email': forms.EmailInput(attrs={'class': 'form-control' , 'id': 'input_email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'id': 'input_phone_number'}), 
            'is_admin': forms.RadioSelect(choices=admin_choices, attrs={'id': 'input_is_admin'}),
        }
