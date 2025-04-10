from django.urls import path
from . import views #imports the views module in the polls app 

#must add IN polls.views bc that is the directory in which views.py is in 
#from polls.views import delivery_rating

app_name = "polls"
"""
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    #new for this project 
    #path('delivery_rating/', delivery_rating, name='delivery_rating'),
    path('delivery_rating/', views.delivery_rating, name='delivery_rating'),
]
    """


urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.ResultsView.as_view(), name="results"),  # Changed DetailView to ResultsView
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("delivery_rating/", views.DeliveryView.as_view(), name="delivery_rating_api"),

    #view the list of delivery Ratings
    path("api/ratings/<int:rating_id>/", views.delivery_rating_detail_api, name="delivery_rating_detail_api"),
    #view the details of a specific delivery rating 
    path("api/ratings/", views.delivery_ratings_list_api, name="delivery_ratings_list_api"),
]
