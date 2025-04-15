from django.core.management.base import BaseCommand
from food.models import Food, Certification, FarmingPractice, ImpactMetric
from django.utils.text import slugify

all_foods_data = [
    {
        'name': 'Apple',
        'food_description': 'Apples are rich in dietary fiber, which aids in digestion and promotes gut health. They also contain powerful antioxidants, such as flavonoids, that can help reduce the risk of chronic diseases like heart disease and diabetes. Apples are also low in calories, making them a satisfying and healthy snack option.',
        'food_origin': 'Our apples are grown at "Harrison Farm" in Kelowna, British Columbia. This local farm embraces regenerative agriculture practices to produce high-quality, nutritious apples.',
        'latitude': 49.8891,
        'longitude': -119.4960,
        'certifications': [
            'food/images/certification1.png',
            'food/images/certification2.png',
            'food/images/certification3.png',
        ],
        'farming_practices': [
            'Organic pest management',
            'Crop rotation to maintain soil health',
            'Water conservation techniques'
        ],
        'impact_metrics': {
            'water_usage': '1,200 liters per kg',
            'co2_emissions': '0.5 kg CO2 per kg',
            'land_use': '0.2 hectares per ton'
        },
        'image': 'food/images/apple.png',
        'purchase_link': 'product-purchase-page-apples.html'
    },
    {
        'name': 'Orange',
        'food_description': 'Known for their high vitamin C content, oranges are perfect for boosting your immune system. They also contain fiber and antioxidants like flavonoids, which support heart health, reduce inflammation, and promote healthy skin. Eating oranges regularly can contribute to overall hydration and skin health as well.',
        'food_origin': 'Grown at "La Ferme des Quatre Vents" in Saint-Antoine-de-Tilly, Quebec, a farm committed to organic farming and eco-friendly practices. This small farm produces high-quality oranges with minimal environmental impact.',
        'latitude': 46.6991,
        'longitude': -71.5967,
        'certifications': [
            'food/images/certification1.png',
            'food/images/certification2.png',
            'food/images/certification3.png',
        ],
        'farming_practices': [
            'Shade-grown cultivation',
            'Natural pest control methods',
            'Soil regeneration techniques'
        ],
        'impact_metrics': {
            'water_usage': '1,500 liters per kg',
            'co2_emissions': '0.4 kg CO2 per kg',
            'land_use': '0.25 hectares per ton'
        },
        'image': 'food/images/orange.png',
        'purchase_link': 'product-purchase-page-oranges.html'
    },
    {
        'name': 'Kiwi',
        'food_description': 'Kiwis are packed with vitamin C, more than an orange, and they also contain vitamins K and E, folate, and potassium. These green fruits are excellent for digestive health due to their enzyme actinidin, which helps break down proteins. Kiwis support immune function, reduce blood pressure, and contribute to skin health.',
        'food_origin': 'Harvested at "Kiwifruit Farms" in the Niagara Region, Ontario, Canada, with high sustainability standards. Known for its commitment to organic farming and eco-friendly practices.',
        'latitude': 43.0896,
        'longitude': -79.0624,
        'certifications': [
            'food/images/certification1.png',
            'food/images/certification2.png',
            'food/images/certification3.png',
        ],
        'farming_practices': [
            'Use of organic fertilizers',
            'Integrated pest management',
            'Biodiversity conservation techniques'
        ],
        'impact_metrics': {
            'water_usage': '1,800 liters per kg',
            'co2_emissions': '0.6 kg CO2 per kg',
            'land_use': '0.3 hectares per ton'
        },
        'image': 'food/images/kiwi.png',
        'purchase_link': 'product-purchase-page-kiwi.html'
    },
    {
        'name': 'Avocados',
        'food_description': 'Avocados are a great source of healthy monounsaturated fats, which are heart-healthy and help in the absorption of fat-soluble vitamins. They also contain fiber, potassium, and antioxidants that support eye health, reduce inflammation, and contribute to maintaining healthy cholesterol levels.',
        'food_origin': 'Grown at "Avocado Oasis" farm in the Essex County, Ontario, Canada. This local farm utilizes drip irrigation systems and focuses on soil health and sustainable land management practices.',
        'latitude': 42.1063,
        'longitude': -82.7610,
        'certifications': [
            'food/images/certification1.png',
            'food/images/certification2.png',
            'food/images/certification3.png',
        ],
        'farming_practices': [
            'Drip irrigation systems to conserve water',
            'Soil health improvement techniques',
            'Responsible land management practices'
        ],
        'impact_metrics': {
            'water_usage': '2,000 liters per kg',
            'co2_emissions': '0.8 kg CO2 per kg',
            'land_use': '0.5 hectares per ton'
        },
        'image': 'food/images/avocado.png',
        'purchase_link': 'product-purchase-page-avocados.html'
    },
    {
        'name': 'Pineapples',
        'food_description': 'Pineapples are rich in vitamin C and bromelain, an enzyme that has anti-inflammatory properties. They aid in digestion, boost immune function, and promote skin health. The high manganese content in pineapples also supports bone health and the metabolism of fats and carbohydrates.',
        'food_origin': 'Harvested at "Pineapple Orchard" in the Fraser Valley, British Columbia, Canada, following sustainable farming practices. This local farm uses agroforestry techniques to protect biodiversity and conserve water.',
        'latitude': 49.0495,
        'longitude': -122.3053,
        'certifications': [
            'food/images/certification1.png',
            'food/images/certification2.png',
            'food/images/certification3.png',
        ],
        'farming_practices': [
            'Natural pest control methods',
            'Agroforestry techniques for soil and biodiversity protection',
            'Water-saving irrigation practices'
        ],
        'impact_metrics': {
            'water_usage': '1,800 liters per kg',
            'co2_emissions': '0.7 kg CO2 per kg',
            'land_use': '0.4 hectares per ton'
        },
        'image': 'food/images/pineapple.png',
        'purchase_link': 'product-purchase-page-pineapple.html'
    },
    {
        'name': 'Blueberries',
        'food_description': 'Blueberries are a powerhouse of antioxidants, particularly rich in anthocyanins that help protect cells from oxidative stress. These tiny berries are great for brain health, improve memory, and are loaded with vitamin C. They are also high in fiber, helping digestion, and can support heart health by reducing blood pressure.',
        'food_origin': 'Cultivated at "Blueberry Ridge Farm" in Langley, British Columbia, Canada, with organic certification and fair trade practices. Known for environmentally conscious farming methods.',
        'latitude': 49.1043,
        'longitude': -122.6615,
        'certifications': [
            'food/images/certification1.png',
            'food/images/certification2.png',
            'food/images/certification3.png',
        ],
        'farming_practices': [
            'Crop rotation for soil health',
            'Minimal pesticide use with integrated pest management',
            'Water conservation practices'
        ],
        'impact_metrics': {
            'water_usage': '1,100 liters per kg',
            'co2_emissions': '0.4 kg CO2 per kg',
            'land_use': '0.2 hectares per ton'
        },
        'image': 'food/images/blueberries.png',
        'purchase_link': 'product-purchase-page-blueberries.html'
    }
]

class Command(BaseCommand):
    help = 'Populates the database with initial food data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting data population...'))

        certifications_cache = {}
        practices_cache = {}
        impact_metrics_cache = {}

        for food_data in all_foods_data:
            # Create or get ImpactMetric
            impact_name = f"{food_data['name']} Metric"
            impact, created = ImpactMetric.objects.get_or_create(
                name=impact_name,
                defaults=food_data['impact_metrics']
            )
            impact_metrics_cache[impact_name] = impact

            # Create or get Food
            food, created = Food.objects.get_or_create(
                name=food_data['name'],
                defaults={
                    'food_description': food_data['food_description'],
                    'food_origin': food_data['food_origin'],
                    'latitude': food_data['latitude'],
                    'longitude': food_data['longitude'],
                    'image': food_data['image'],
                    'purchase_link': food_data['purchase_link'],
                    'impact_metric': impact,
                    'slug': slugify(food_data['name']),
                }
            )

            # Add Certifications
            for cert_path in food_data['certifications']:
                certification, created = Certification.objects.get_or_create(image=cert_path)
                if certification not in food.certifications.all():
                    food.certifications.add(certification)

            # Add Farming Practices
            for practice_name in food_data['farming_practices']:
                practice, created = FarmingPractice.objects.get_or_create(name=practice_name)
                if practice not in food.farming_practices.all():
                    food.farming_practices.add(practice)

            food.save()

        self.stdout.write(self.style.SUCCESS('Data population complete.'))