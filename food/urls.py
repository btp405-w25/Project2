from django.urls import path
from . import views

urlpatterns = [
    path("foods", views.index, name="foods-page"), #/foods/
    path('foods/<slug:slug>', views.food_detail, name="food-detail-page"),
    path('foods/certification/<str:certification_name>', views.organicCertification, name="organic-certification")
]
