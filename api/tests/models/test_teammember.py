from django.test import TestCase

from api.models import TeamMember

class TeammeberModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        TeamMember.objects.create(
            first_name='Pad',
            last_name='Thai',
            email='pad_thai@yum.thai',
            phone_number='123-456-7890',
            is_admin = True
        )

    def test_field_constraints(self):
        teammember = TeamMember.objects.get(id=1)

        # test max length for first name
        first_name_max_length = teammember._meta.get_field('first_name').max_length
        self.assertEqual(first_name_max_length, 50)

        # test max length for last name
        last_name_max_length = teammember._meta.get_field('last_name').max_length
        self.assertEqual(last_name_max_length, 50)

        # test max length for email
        email_max_length = teammember._meta.get_field('email').max_length
        self.assertEqual(email_max_length, 255)

        # test max length for phone number 
        phone_number_max_length = teammember._meta.get_field('phone_number').max_length
        self.assertEqual(phone_number_max_length, 12)