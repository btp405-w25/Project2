"""
here the test dataset is created and then destroyed so taht is why you wont see it in the admin panel 
to run the tests run the command:
python manage.py test
"""

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Vendor, DeliveryRating
from datetime import date

class DeliveryRatingTests(TestCase):
    def setUp(self):
        #creates a test user 
        self.user = User.objects.create_user(username='testuser', password='12345')
        #creates a test vendor 
        self.vendor = Vendor.objects.create(name='Goodfood')

    def test_create_delivery_rating(self):
        #creates a delivery rating & sets all fields of that class 
        rating = DeliveryRating.objects.create(
            user=self.user,
            vendor=self.vendor,
            rating=4,
            review_text="Fast and eco-friendly delivery!",
            delivery_date=date.today(),
            eco_friendly_packaging=True
        )
        self.assertEqual(rating.rating, 4) #checks if the rating is correctlu saved as the val 4
        self.assertEqual(rating.vendor.name, 'Goodfood') #checks that the saved vendor name is indeed Goodood
