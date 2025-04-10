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
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class DeliveryRating(models.Model):
   #ERRORS with this, the list of stars is inverted, when I cclick one start I get 5 stars and when I do 5 stars, it says I chose 1 star
   #RATING_CHOICES = [(i, f"{i} ⭐") for i in range(1, 6)] 
   #CORRECT bc the last 5 = 5th star is at the top of the list 
   #the star = just gets displayed in the user input data 
    RATING_CHOICES = [(i, f"{i} ⭐") for i in range(5, 0,-1)] #reverses the list to so last star = 5 stars, it generates 5 nums from 5 to 1, and decreasesthe num by -1 eacg time

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)  
    review_text = models.TextField(blank=True)
    delivery_date = models.DateField()
    eco_friendly_packaging = models.BooleanField(default=False)
    image = models.ImageField(upload_to='ratings/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user} rated {self.vendor} - {self.rating}⭐"
