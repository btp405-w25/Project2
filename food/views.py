# food/views.py
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Food, Certification

def index(request):
    foods = Food.objects.all().values() # Serialize queryset to list of dicts
    return JsonResponse(list(foods), safe=False)

def food_detail(request, slug):
    food = get_object_or_404(Food, slug=slug)
    food_data = {
        'name': food.name,
        'food_description': food.food_description,
        'food_origin': food.food_origin,
        'latitude': food.latitude,
        'longitude': food.longitude,
        'image': food.image.url if food.image else None,
        'purchase_link': food.purchase_link,
        'slug': food.slug,
        'certifications': [{'name': c.name, 'image': c.image.url if c.image else None} for c in food.certifications.all()],
        'farming_practices': [{'name': fp.name} for fp in food.farming_practices.all()],
        'impact_metric': {'water_usage': food.impact_metric.water_usage, 'co2_emissions': food.impact_metric.co2_emissions, 'land_use': food.impact_metric.land_use} if food.impact_metric else None,
    }
    return JsonResponse(food_data)

def organicCertification(request, certification_name):
    certification = get_object_or_404(Certification, name=certification_name)
    certification_data = {
        'name': certification.name,
        'image': certification.image.url if certification.image else None,
        'certification_description': certification.certification_description,
    }
    return JsonResponse(certification_data)