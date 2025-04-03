"""
#setup code from official django website 
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
        
"""

import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text  # Removed the stray double quote



class Vendor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class DeliveryRating(models.Model):
    """had to add bc of IntegrityError at /polls/delivery_rating/
    NOT NULL constraint failed: polls_deliveryrating.user_id"""
    # allows user field to be optoonnal 
    #user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]  # 1 to 5 stars

    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name="ratings")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    review_text = models.TextField(blank=True, null=True)
    delivery_date = models.DateField()
    eco_friendly_packaging = models.BooleanField(default=False)
    #lets the user upload an image, upload_to="ratings/ = IS WHERE THE IMG GETS STORED, blank=True  = means field is optional, null=True = means u can store nulll in the database
    image = models.ImageField(upload_to="ratings/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.vendor.name} - {self.rating} Stars"
