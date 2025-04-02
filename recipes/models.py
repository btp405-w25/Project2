from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    season = models.CharField(max_length=50)  # Example: 'Spring', 'Summer'
    location = models.CharField(max_length=100)  # Example: 'California'

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    main_ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    ingredients = models.TextField()
    instructions = models.TextField()
    dietary_preferences = models.CharField(
        max_length=50,
        choices=[
            ('vegan', 'Vegan'),
            ('vegetarian', 'Vegetarian'),
            ('gluten-free', 'Gluten-Free'),
            ('none', 'No Preference')
        ]
    )
    carbon_footprint = models.FloatField()  # Example: total CO2 emissions for the recipe
    
    def __str__(self):
        return self.name
    
    @classmethod
    def get_seasonal_recipes(cls, location, season):
        """
        Get seasonal recipes based on location and season.
        """
        # Filter ingredients based on location and season
        available_ingredients = Ingredient.objects.filter(
            location=location,
            season=season
        )

        # Get recipes that use those ingredients in the main ingredient or ingredients list
        seasonal_recipes = cls.objects.filter(
            main_ingredient__in=available_ingredients
        ).distinct()

        return seasonal_recipes  