from django.db import models
from django.utils.text import slugify

# Create your models here.
# models.py
class Certification(models.Model):
  name = models.CharField(max_length=30,default="certification")
  image = models.ImageField(upload_to='food/images/')
  certification_description = models.TextField(default="")
  def __str__(self):
    return self.name


class FarmingPractice(models.Model):
  name = models.CharField(max_length=100)
  def __str__(self):
    return self.name

class ImpactMetric(models.Model):
  name = models.CharField(max_length=30,default="ImpactMetric")
  water_usage = models.CharField(max_length=30)
  co2_emissions = models.CharField(max_length=30)
  land_use = models.CharField(max_length=30)
  def __str__(self):
    return self.name


class Food(models.Model):
  name = models.CharField(max_length=50)
  food_description = models.TextField()
  food_origin = models.TextField()
  latitude = models.FloatField()
  longitude = models.FloatField()
  image = models.ImageField(upload_to='food/images/')
  purchase_link = models.URLField()
  slug = models.SlugField(default="", null=False)
  
  certifications = models.ManyToManyField(Certification)
  farming_practices = models.ManyToManyField(FarmingPractice)
  impact_metric = models.ForeignKey(ImpactMetric, on_delete=models.SET_NULL, null=True, related_name="foods")

  def __str__(self):
      return self.name
    
  def save(self, *args, **kwargs):
    self.slug = slugify(self.name)
    super().save(*args, **kwargs)

  
