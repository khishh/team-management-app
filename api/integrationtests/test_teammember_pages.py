from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from contextlib import contextmanager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of
import time

@contextmanager
def wait_for_page_load(driver, timeout=30):
    old_page = driver.find_element(By.TAG_NAME, 'html')
    yield
    WebDriverWait(driver, timeout).until(staleness_of(old_page))


def fill_out_teammebmer_form_and_submit(
        driver: webdriver, member_info: dict):
    print(member_info)
    driver.find_element(By.ID, 'input_first_name').clear()
    driver.find_element(By.ID, 'input_first_name').send_keys(
        member_info['first_name'])
    driver.find_element(By.ID, 'input_last_name').clear()
    driver.find_element(By.ID, 'input_last_name').send_keys(
        member_info['last_name'])
    driver.find_element(By.ID, 'input_email').clear()
    driver.find_element(By.ID, 'input_email').send_keys(
        member_info['email'])
    driver.find_element(By.ID, 'input_phone_number').clear()
    driver.find_element(By.ID, 'input_phone_number').send_keys(
        member_info['phone_number'])

    if member_info['is_admin'] == True:
        driver.find_element(By.ID, 'input_is_admin_1').click()
    else:
        driver.find_element(By.ID, 'input_is_admin_0').click()

    with wait_for_page_load(driver, 10):
        driver.find_element(By.ID, 'teammember-submit-btn').click()


def verify_teammember_info(
        testcase: LiveServerTestCase, driver: webdriver, member_info: dict, idx: int):
    print(len(driver.find_elements(
        By.CLASS_NAME, 'teammember-list-wrapper')))
    member_wrapper = driver.find_elements(
        By.CLASS_NAME, 'teammember-list-wrapper')[idx]
    teammember_name_wrapper = member_wrapper.find_element(
        By.CLASS_NAME, 'teammember-name')
    testcase.assertEqual(
        teammember_name_wrapper.text,
        f'{member_info["first_name"]} {member_info["last_name"]} (Admin)' if member_info[
            'is_admin']
        else f'{member_info["first_name"]} {member_info["last_name"]}'
    )
    testcase.assertEqual(
        member_wrapper.find_element(
            By.CLASS_NAME, 'teammember-phone-number').text,
        member_info['phone_number']
    )
    testcase.assertEqual(
        member_wrapper.find_element(
            By.CLASS_NAME, 'team-member-email').text,
        member_info['email']
    )


class TeamMemberPages(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Chrome()
        now = int(time.time())
        cls.new_teammember_info = {
            'first_name': 'Integration',
            'last_name': f'User {now}',
            'email': f'integration_test_{now}@test.com',
            'phone_number': '123-456-7890',
            'is_admin': True if now % 2 == 0 else False
        }

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def testTeamMemberListContent(self):
        self.driver.get('http://localhost:8000/')

        # check title and headers
        self.assertEqual(self.driver.title, 'Team Management App')

        num_of_teammembers = len(self.driver.find_elements(
            By.CLASS_NAME, 'teammember-list-wrapper'))

        self.assertEqual(self.driver.find_element(
            By.CLASS_NAME, 'page-header').text, 'Team Members')
        self.assertEqual(self.driver.find_element(
            By.CLASS_NAME, 'page-subheader').text, f'You have {num_of_teammembers} team members.')

        #  check add new member button
        add_member_btn = self.driver.find_element(
            By.ID, 'add-member-btn')
        self.assertIsNotNone(add_member_btn)
        self.assertEqual(add_member_btn.text, 'Add new member')

    def testAddNewMemberScenario(self):
        self.driver.get('http://localhost:8000/')
        add_member_btn = self.driver.find_element(
            By.ID, 'add-member-btn')

        with wait_for_page_load(self.driver, 10):
            add_member_btn.click()

        # check the current url
        self.assertTrue(self.driver.current_url,
                        f'http://localhost:8000/add')

        # fill out the form and submit

        fill_out_teammebmer_form_and_submit(
            driver=self.driver,
            member_info=self.new_teammember_info
        )

        # check the current url after redirect
        self.assertTrue(self.driver.current_url,
                        f'http://localhost:8000/')

        # check the newly added user info
        verify_teammember_info(
            testcase=self,
            driver=self.driver,
            member_info=self.new_teammember_info,
            idx=-1
        )

    def testEditMemberScenario(self):
        self.driver.get('http://localhost:8000/')

        teammember_idx = 0

        # move to edit page
        with wait_for_page_load(self.driver, 10):
            self.driver.find_elements(
                By.CLASS_NAME, 'teammember-list-wrapper')[teammember_idx].click()

        # check the current url after redirect
        self.assertRegex(self.driver.current_url,
                         r'^http://localhost:8000/[0-9]{1,}/edit')

        now = int(time.time())
        edit_member_info = {
            'first_name': 'Integration!',
            'last_name': f'User {now} Edited',
            'email': f'integration_test_{now}_edited@test.com',
            'phone_number': '098-765-4321',
            'is_admin': False if now % 2 == 0 else True
        }
        fill_out_teammebmer_form_and_submit(
            driver=self.driver,
            member_info=edit_member_info
        )

        # check the current url after redirect
        self.assertTrue(self.driver.current_url,
                        f'http://localhost:8000/')

        
        # check the newly added user info
        verify_teammember_info(
            testcase=self,
            driver=self.driver,
            member_info=edit_member_info,
            idx=teammember_idx
        )

    def testDeleteMemberScenario(self):
        self.driver.get('http://localhost:8000/')

        teammember_idx = 0
        num_of_teammembers = len(self.driver.find_elements(
            By.CLASS_NAME, 'teammember-list-wrapper'))
        first_member_wrapper = self.driver.find_elements(
            By.CLASS_NAME, 'teammember-list-wrapper')[teammember_idx]
        first_member_name = first_member_wrapper.find_element(By.CLASS_NAME, 'teammember-name').text

        # move to edit page
        with wait_for_page_load(self.driver, 10):
            self.driver.find_elements(
                By.CLASS_NAME, 'teammember-list-wrapper')[teammember_idx].click()

        # check the current url after redirect
        self.assertRegex(self.driver.current_url,
                         r'^http://localhost:8000/[0-9]{1,}/edit')

        self.driver.find_element(By.ID, 'teammember-delete-btn').click()

         # check the current url after redirect
        self.assertTrue(self.driver.current_url,
                        f'http://localhost:8000/')

        first_member_wrapper = self.driver.find_elements(
            By.CLASS_NAME, 'teammember-list-wrapper')[teammember_idx]

        first_member_name_after_delete = first_member_wrapper.find_element(By.CLASS_NAME, 'teammember-name').text

        self.assertNotEqual(first_member_name, first_member_name_after_delete)
        self.assertEqual(len(self.driver.find_elements(
                By.CLASS_NAME, 'teammember-list-wrapper')), num_of_teammembers-1)
