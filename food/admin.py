from django.contrib import admin

# Register your models here.
from .models import Food, Certification, FarmingPractice, ImpactMetric


admin.site.register(Food)
admin.site.register(Certification)
admin.site.register(FarmingPractice)
admin.site.register(ImpactMetric)