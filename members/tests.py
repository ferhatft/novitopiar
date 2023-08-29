from django.test import TestCase
from django.urls import reverse
from .models import Organization, User
from django.contrib.auth import get_user_model

class OrganizationModelTest(TestCase):

    def setUp(self):
        self.org = Organization.objects.create(
            name="TestOrg",
            org_type="SME",
            country="Turkey",
            foundation_date="2023-01-01",
            employee_count=50
        )

    def test_organization_creation(self):
        self.assertEqual(self.org.name, "TestOrg")
        self.assertEqual(self.org.org_type, "SME")

class OrganizationViewTest(TestCase):

    def setUp(self):
        self.org = Organization.objects.create(
            name="TestOrg",
            org_type="SME",
            country="Turkey",
            foundation_date="2023-01-01",
            employee_count=50
        )
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')

    def test_organization_list_view(self):
        response = self.client.get(reverse('api-organization-list-create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "TestOrg")

    def test_organization_filter_view(self):
        response = self.client.get(reverse('api-organization-filter'), {
            'name': 'TestOrg',
            'org_type': 'SME',
            'country': 'Turkey',
            'start_date': '2020-01-01',
            'end_date': '2025-01-01',
            'min_employee_count': 10,
            'max_employee_count': 100
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "TestOrg")

    # ... Add more view tests here as needed

class UserTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')

    # ... Add more user tests or other tests as needed



#python manage.py test members
