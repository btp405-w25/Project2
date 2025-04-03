



"""
from django import forms 
from .models import Choice #Choice = represents poll options in the database 

class Form(forms.Form):  #class inherits forms.Form
    choice = forms.ModelChoiceField( #= a form field in which a user can select a Choice obj 
        queryset=Choice.objects.none(), #sets the queryset to empty 
        widget=forms.RadioSelect, #change ste default dropdown to a radiobutton select 
        empty_label=None, #removes the default "select an option" placeholder bc this is a radio buttpmn
        label="Select your choice"
    )

    def __init__(self, question, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['choice'].queryset = question.choice_set.all()"
        """

#diff form not radio buttton s

#model = python class that represents a database table
#DeliveryRating = from my models.py 

from django import forms 
from .models import DeliveryRating, Vendor # import  the 2 models from the app's models.py file 
from django.contrib.auth.models import User
from .models import DeliveryRating  # Import your model here


class DeliveryRatingForm(forms.ModelForm): #creates a form class that is linked to the DeliveryRating model

    """
    WRITE THIS IN THE SHELL TO GENERATE
    from polls.models import Vendor

    #list of ecologicalgreen vendors
    green_vendors= ['The Conscious Farm Kitchen', 'BIO RAW','Goodfood', 'Hellofresh', 'Green Cherf', 'SkipTheDishes']
    for i in green_vendors: # for every item in the array, create a new vendor & set the vendors name to the name value in the arr
        Vendor.objects.create(name=i)
    """
    
    """
    Froom stackoverflow: 
    Model Meta is basically the inner class of your model class. Model Meta is basically used to change the 
    behavior of your model fields like changing order options, 
    verbose_name, and a lot of other options. It’s completely optional to add a Meta class to your model.
    """
    class Meta: # nested class that configures how the form behaves 
        model = DeliveryRating #says that the form is based on the DeliveryRating model
        #all fields in the form 
        fields = ["vendor", "rating", "review_text", "delivery_date", "eco_friendly_packaging", "image"]
        #this is to show a calendar 
        widgets = {
            "delivery_date": forms.DateInput(attrs={"type": "date"}),
            #doesnt xactly work, star doesnt work 
            "rating": forms.RadioSelect(choices=[(i, f"{i} ⭐") for i in range(1, 6)]),
        }

    """had to add bc of IntegrityError at /polls/delivery_rating/
    NOT NULL constraint failed: polls_deliveryrating.user_id"""

    """
    # allows user field to be optoonnal 
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=False, widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].required = False  # Make the user field optional
        """