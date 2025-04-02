from django.contrib import admin
from .models import Recipe, Ingredient

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'season', 'location')  # Display these fields in the list view
    search_fields = ('name', 'season', 'location')  # Add search functionality for these fields
    list_filter = ('season', 'location')  # Add filters for season and location

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'main_ingredient','get_ingredients', 'dietary_preferences', 'carbon_footprint')  # Display these fields in the list view
    search_fields = ('name', 'dietary_preferences')  # Add search functionality for these fields
    list_filter = ('dietary_preferences',)  # Add a filter for dietary preferences

    def get_ingredients(self, obj):
        return obj.ingredients 
    get_ingredients.short_description = 'Ingredients'  # Customize the column title

# Register your models with the custom admin classes
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
