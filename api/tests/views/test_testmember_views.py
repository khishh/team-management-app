from django.test import TestCase

from api.models import TeamMember

num_of_teammember = 10


class TeamMamberListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:

        for teammember_id in range(num_of_teammember):
            TeamMember.objects.create(
                first_name=f'User{teammember_id}',
                last_name=f'Test{teammember_id}',
                email=f'user{teammember_id}@test.com',
                phone_number='123-456-7890',
                is_admin=True if teammember_id % 2 == 0 else False
            )

    def test_list_view_url_exist(self):
        response = self.client.get('/teammembers/')
        self.assertEqual(response.status_code, 200)

    def test_list_view_verify_template(self):
        response = self.client.get('/teammembers/')
        self.assertTemplateUsed(response, 'teammembers/teammember_list.html')

    def test_list_all_teammember(self):
        response = self.client.get('/teammembers/')
        teammembers = response.context['team_members']
        self.assertTrue(len(teammembers), num_of_teammember)

        count = 0
        for teammember in teammembers:
            self.assertTrue(teammember.first_name, f'User{count}')
            self.assertTrue(teammember.last_name, f'Test{count}')
            self.assertTrue(teammember.email, f'user{count}@test.com')
            self.assertTrue(teammember.email, f'123-456-7890')
            self.assertEqual(teammember.is_admin, True if count %
                             2 == 0 else False)
            count = count + 1