from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

class AccountsTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create test user
        self.test_user = User.objects.create_user(
            username='existinguser',
            password='testpass123',
            email='existing@test.com'
        )
    def test_user_registration(self):
        """Test user registration functionality"""
        data = {
            'username': 'newtestuser',  
            'email': 'newtest@example.com',
            'password': 'TestPass123!',
            'password2':'TestPass123!'
        }
        response = self.client.post(
            reverse('register'),
            data,
            format='json'
        )
        self.assertEqual(
            response.status_code, 
            status.HTTP_201_CREATED,
            msg=f"Expected 201, got {response.status_code}. Response data: {response.data}"
        )
        self.assertTrue('token' in response.data)
        self.assertEqual(response.data['user']['username'], 'newtestuser')
        # Verify user was actually created
        self.assertTrue(
            User.objects.filter(username='newtestuser').exists()
        )

    def test_user_registration_invalid_data(self):
        """Test registration with invalid data"""
        data = {
            'username': '',  # Invalid: empty username
            'email': 'invalid-email',  # Invalid email format
            'password': '123'  # Too short password
        }
        response = self.client.post(reverse('register'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_registration_password_mismatch(self):
        """Test registration with mismatched passwords"""
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'TestPass123!',
            'password2': 'DifferentPass123!'
        }
        response = self.client.post(reverse('register'), data, format='json')
        self.assertEqual(
            response.status_code, 
            status.HTTP_400_BAD_REQUEST,
            "Registration should fail when passwords don't match"
        )

    def test_user_registration_invalid_email(self):
        """Test registration with invalid email format"""
        data = {
            'username': 'testuser',
            'email': 'invalid-email',
            'password': 'TestPass123!',
            'password2': 'TestPass123!'
        }
        response = self.client.post(reverse('register'), data, format='json')
        self.assertEqual(
            response.status_code, 
            status.HTTP_400_BAD_REQUEST,
            "Registration should fail with invalid email"
        )

    def test_user_login_success(self):
        """Test successful user login"""
        data = {
            'username': 'existinguser',
            'password': 'testpass123'
        }
        response = self.client.post(
            reverse('login'),  
            data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)
        self.assertEqual(response.data['user']['username'], 'existinguser')

    def test_user_login_invalid_credentials(self):
        """Test login with invalid credentials"""
        data = {
            'username': 'existinguser',
            'password': 'wrongpassword'
        }
        response = self.client.post(reverse('login'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], 'Invalid credentials')

    def test_duplicate_username_registration(self):
        """Test registration with existing username"""
        data = {
            'username': 'existinguser',
            'email': 'new@test.com',
            'password': 'NewPass123!'
        }
        response = self.client.post(reverse('register'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_login_missing_fields(self):
        """Test login with missing fields"""
        data = {'username': 'existinguser'}  # Missing password
        response = self.client.post(reverse('login'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_login_with_wrong_username(self):
        """Test login attempt with non-existent username"""
        data = {
            'username': 'nonexistentuser',
            'password': 'testpass123'
        }
        response = self.client.post(reverse('login'), data, format='json')
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
            "Should reject login with non-existent username"
        )

    def test_registration_with_existing_email(self):
        """Test registration with an email that's already in use"""
        data = {
            'username': 'newuser',
            'email': 'existing@test.com',  # Email already used in setUp
            'password': 'TestPass123!',
            'password2': 'TestPass123!'
        }
        response = self.client.post(reverse('register'), data, format='json')
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
            "Should reject registration with duplicate email"
        )
