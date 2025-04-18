from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Ingredient

class IngredientViewSetTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create test data
        Ingredient.objects.create(name="Tomato", season="Summer", location="Calgary")
        Ingredient.objects.create(name="Corn", season="Summer", location="Calgary")
        Ingredient.objects.create(name="Potato", season="Winter", location="Toronto")

    def test_filter_by_location_and_season(self):
        response = self.client.get("/api/ingredients/?location=Calgary&season=Summer")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["name"], "Tomato")
        self.assertEqual(response.data[1]["name"], "Corn")

    def test_filter_by_location_only(self):
        response = self.client.get("/api/ingredients/?location=Toronto")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Potato")

    def test_filter_by_season_only(self):
        response = self.client.get("/api/ingredients/?season=Winter")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Potato")

    def test_no_filters(self):
        response = self.client.get("/api/ingredients/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_no_results(self):
        response = self.client.get("/api/ingredients/?location=Vancouver&season=Spring")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
