from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Ingredient, Recipe
from .serializer import IngredientSerializer, RecipeSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    def list(self, request):
        location = request.GET.get('location', None)
        season = request.GET.get('season', None)

        # Apply filtering logic
        if location and season:
            ingredients = Ingredient.objects.filter(location=location, season=season)
        elif location:
            ingredients = Ingredient.objects.filter(location=location)
        elif season:
            ingredients = Ingredient.objects.filter(season=season)
        else:
            ingredients = Ingredient.objects.all()

        # Ensure we're passing a queryset of Ingredient objects to the serializer
        serializer = self.get_serializer(ingredients, many=True)
        return Response(serializer.data)



class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_queryset(self):
        location = self.request.query_params.get('location', None)
        season = self.request.query_params.get('season', None)

        queryset = super().get_queryset()

        if location and season:
            queryset = queryset.filter(
                main_ingredient__location=location,
                main_ingredient__season=season
            ).distinct()

        return queryset

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        # Modify ingredients before sending response
        data = serializer.data
        for recipe in data:
            recipe['ingredients'] = recipe['ingredients'].split(",") if recipe['ingredients'] else []
        
        return Response(data)
