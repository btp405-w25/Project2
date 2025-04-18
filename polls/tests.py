from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import DeliveryRating, Vendor
from datetime import date

class DeliveryRatingTests(TestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpass123'
        )
        # Create test vendor
        self.vendor = Vendor.objects.create(name='TestVendor')
        # Create test delivery rating
        self.rating = DeliveryRating.objects.create(
            user=self.user,
            vendor=self.vendor,
            rating=5,
            review_text="Great delivery service!",
            delivery_date=date.today(),
            eco_friendly_packaging=True
        )
        # Setup API client
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
    def test_create_delivery_rating(self):
        """Test creating a new delivery rating"""
        data = {
            'vendor': self.vendor.name,
            'rating': 4,
            'review_text': 'Good service',
            'delivery_date': date.today().isoformat(),
            'eco_friendly_packaging': True
        }     
        response = self.client.post(
            reverse('polls:delivery_rating_api'),
            data,
            format='json'
        )  
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(DeliveryRating.objects.count(), 2)
    def test_get_delivery_rating_detail(self):
        """Test retrieving a specific delivery rating"""
        response = self.client.get(
            reverse('polls:delivery_rating_detail_api', 
            kwargs={'rating_id': self.rating.id})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['rating'], 5)
        self.assertEqual(response.data['review_text'], "Great delivery service!")
    def test_get_delivery_ratings_list(self):
        """Test retrieving all delivery ratings"""
        response = self.client.get(reverse('polls:delivery_ratings_list_api')) 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    def test_unauthorized_access(self):
        """Test unauthorized access to delivery rating endpoints"""
        self.client.logout()
        data = {
            'vendor': self.vendor.name,
            'rating': 4,
            'review_text': 'Good service',
            'delivery_date': date.today().isoformat(),
            'eco_friendly_packaging': True
        }
        
        response = self.client.post(
            reverse('polls:delivery_rating_api'),
            data,
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_invalid_rating_value(self):
        """Test creating a rating with invalid value"""
        data = {
            'vendor': self.vendor.name,
            'rating': 6,  # Invalid rating (should be 1-5)
            'review_text': 'Good service',
            'delivery_date': date.today().isoformat(),
            'eco_friendly_packaging': True
        }
        
        response = self.client.post(
            reverse('polls:delivery_rating_api'),
            data,
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_vendor_str_representation(self):
        """Test string representation of Vendor model"""
        self.assertEqual(str(self.vendor), 'TestVendor')

    def test_delivery_rating_str_representation(self):
        """Test string representation of DeliveryRating model"""
        expected_str = f"{self.user} rated {self.vendor} - 5⭐"
        self.assertEqual(str(self.rating), expected_str)
