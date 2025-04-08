from django.contrib import admin


from .models import Choice, Question
from .models import DeliveryRating


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]

class DeliveryRatingAdmin(admin.ModelAdmin): # admin.ModelAdmin) = django class that controls how models behave in django 
    #the names of columns = aka the fields that appear in my admin 
    list_display = ('user', 'vendor', 'rating', 'delivery_date', 'eco_friendly_packaging')
    #I can filer the user entries by these fields,this appears as a separate column on the right side of the screen
    list_filter = ('vendor', 'rating', 'delivery_date')
    #username for now is just "admin"
    #lets me search using a search box I can search via the person's username and any text in the review itself 
    search_fields = ('user__username', 'review_text')
    readonly_fields = ('created_at',) # shows the  created date that the review was submiteed but does not let me edit it 

admin.site.register(Question, QuestionAdmin)
admin.site.register(DeliveryRating, DeliveryRatingAdmin) #DeliveryRatingAdmin= name of class made in this file 