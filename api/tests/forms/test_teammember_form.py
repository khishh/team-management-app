from django.test import TestCase

from api.models import TeamMember
from api.forms import TeamMemberForm

class TeamMemberFormTest(TestCase):

    def test_teammember_form_with_valid_data(self):
        form = TeamMemberForm(
            data={
                'first_name': 'Pad',
                'last_name': 'Thai',
                'email': 'pad_thai@yum.thai',
                'phone_number': '123-456-7890',
                'is_admin': True
            }
        )

        self.assertTrue(form.is_valid())

    def test_teammember_form_with_invalid_email(self):
        form = TeamMemberForm(
            data={
                'first_name': 'Pad',
                'last_name': 'Thai',
                'email': 'pad_thai',
                'phone_number': '123-456-7890',
                'is_admin': True
            }
        )

        self.assertFalse(form.is_valid())

    def test_teammember_form_with_invalid_email(self):
        form = TeamMemberForm(
            data={
                'first_name': 'Pad',
                'last_name': 'Thai',
                'email': 'pad_thai@yum.thai',
                'phone_number': '1234567890',
                'is_admin': True
            }
        )

        self.assertFalse(form.is_valid())