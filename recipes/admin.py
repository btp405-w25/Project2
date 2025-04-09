from django.contrib import admin
from .models import Recipe, Ingredient

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'season', 'location') 
    search_fields = ('name', 'season', 'location') 
    list_filter = ('season', 'location')  

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'main_ingredient','get_ingredients', 'dietary_preferences', 'carbon_footprint') 
    search_fields = ('name', 'dietary_preferences') 
    list_filter = ('dietary_preferences',) 
    def get_ingredients(self, obj):
        return obj.ingredients 
    get_ingredients.short_description = 'Ingredients'  # Customize the column title

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
