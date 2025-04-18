from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from food.models import Food, Certification, FarmingPractice, ImpactMetric

class FoodModuleTests(TestCase):
    def setUp(self):
        # Create test image
        self.test_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'',
            content_type='image/jpeg'
        )
        # Create test certification
        self.certification = Certification.objects.create(
            name="Organic",
            image=self.test_image,
            certification_description="Test certification"
        )
        # Create test farming practice
        self.farming_practice = FarmingPractice.objects.create(
            name="Sustainable farming"
        )
        # Create test impact metric
        self.impact_metric = ImpactMetric.objects.create(
            name="Apple Impact",
            water_usage="1,000 liters per kg",
            co2_emissions="0.4 kg CO2 per kg",
            land_use="0.3 hectares per ton"
        )
        # Create test food item
        self.food = Food.objects.create(
            name="Test Apple",
            food_description="Test description",
            food_origin="Test origin",
            latitude=49.8891,
            longitude=-119.4960,
            image=self.test_image,
            purchase_link="http://example.com",
            impact_metric=self.impact_metric
        )
        self.food.certifications.add(self.certification)
        self.food.farming_practices.add(self.farming_practice)

    def test_food_list_endpoint(self):
        """Test the food list endpoint"""
        response = self.client.get(reverse('foods-page'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_food_detail_endpoint(self):
        """Test the food detail endpoint"""
        response = self.client.get(reverse('food-detail-page', kwargs={'slug': self.food.slug}))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['name'], 'Test Apple')
        self.assertEqual(data['food_description'], 'Test description')
        self.assertTrue('certifications' in data)
        self.assertTrue('farming_practices' in data)
        self.assertTrue('impact_metric' in data)

    def test_certification_endpoint(self):
        """Test the certification endpoint"""
        response = self.client.get(
            reverse('organic-certification', kwargs={'certification_name': 'Organic'})
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], 'Organic')

    def test_food_slug_generation(self):
        """Test automatic slug generation for food items"""
        food = Food.objects.create(
            name="Test Food Item",
            food_description="Description",
            food_origin="Origin",
            latitude=0,
            longitude=0,
            image=self.test_image,
            purchase_link="http://example.com"
        )
        self.assertEqual(food.slug, 'test-food-item')

    def test_model_string_representations(self):
        """Test string representation of models"""
        self.assertEqual(str(self.food), 'Test Apple')
        self.assertEqual(str(self.certification), 'Organic')
        self.assertEqual(str(self.farming_practice), 'Sustainable farming')
        self.assertEqual(str(self.impact_metric), 'Apple Impact')

    def test_food_relationships(self):
        """Test relationships between food and related models"""
        self.assertEqual(self.food.certifications.count(), 1)
        self.assertEqual(self.food.farming_practices.count(), 1)
        self.assertIsNotNone(self.food.impact_metric)

    def test_invalid_food_detail_request(self):
        """Test requesting non-existent food item"""
        response = self.client.get(reverse('food-detail-page', kwargs={'slug': 'non-existent'}))
        self.assertEqual(response.status_code, 404)

    def test_impact_metric_data(self):
        """Test impact metric data accuracy"""
        self.assertEqual(self.food.impact_metric.water_usage, "1,000 liters per kg")
        self.assertEqual(self.food.impact_metric.co2_emissions, "0.4 kg CO2 per kg")
        self.assertEqual(self.food.impact_metric.land_use, "0.3 hectares per ton")
