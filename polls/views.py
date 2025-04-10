from django.db.models import F
from django.http import  HttpResponseRedirect, HttpResponseBadRequest, JsonResponse # Import HttpResponseBadRequest from django.http
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import DeliveryRating
from .forms import DeliveryRatingForm
from .models import Choice, Question
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import DeliveryRatingSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView

@api_view(['GET'])
def delivery_rating_detail_api(request, rating_id):
    """API endpoint to view a specific delivery rating."""
    try:
        rating = get_object_or_404(DeliveryRating, pk=rating_id)
        serializer = DeliveryRatingSerializer(rating)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def delivery_ratings_list_api(request):
    """API endpoint to list all delivery ratings."""
    ratings = DeliveryRating.objects.all()
    serializer = DeliveryRatingSerializer(ratings, many=True)
    return Response(serializer.data)

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {"latest_question_list": latest_question_list}
#     return render(request, "polls/index.html", context)

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"
    def get_queryset(self):
        """
        #Return the last five published questions (not including those set to be
        #published in the future).
"""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
            :5
        ]

# class DetailView(generic.DetailView):
#     model = Question
#     template_name = "polls/detail.html"
#     def get_queryset(self):
#         """
#        # Excludes any questions that aren't published yet.
# """
#         return Question.objects.filter(pub_date__lte=timezone.now())

class DeliveryView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = DeliveryRatingSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Assuming 'user' should be associated
            return Response({'message': 'Delivery rating submitted successfully!'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

#for form, not from documentation 


#takes an http request as an argument 
"""
def delivery_rating(request):
    return HttpResponse("This is the delivery rating page.") # when a browser visits this page this is what they will see 
"""

# for later I will make  login required 
# LAter I can specify the url, ex: 
# @login_required(lgin_url="/users/login/")
@login_required
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delivery_rating(request):
    if request.method == "POST": #if form submission happens 
        form = DeliveryRatingForm(request.POST, request.FILES) # make an instance of DeliveryRatingForm
        if form.is_valid(): # if all needed fields are filled out 
            #rating if I just want to save the rating ex:
#            rating = form.save(commit=False)
            # also saves form BUT object isnt saved to dtb yet this is needed if I add in the logged in user logic 
            # form = form.save(commit=False)
            #TO ADD LATER = associate user of dtb TO A LOGGED IN USER 
            # form.user = request.user  # Assign the logged-in user
            # form.save() #save data to dtb 
            # return redirect("/")  # Redirect to the admin page  or another page
            form.instance.user = request.user
            form.save()
            # Send a JSON success response
            return JsonResponse({'message': 'Delivery rating submitted successfully!'}, status=201)
    else:
          # For non-POST requests, indicate that only POST is allowed
        return HttpResponseBadRequest("Only POST requests are allowed for this endpoint.")

# @login_required
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def delivery_rating(request):
#     if request.method == "POST":
#         form = DeliveryRatingForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.instance.user = request.user
#             form.save()
#             # Send a JSON success response
#             return JsonResponse({'message': 'Delivery rating submitted successfully!'}, status=201)
#         else:
#             print("Form Errors:", form.errors)
#             # Send a JSON error response with form errors
#             return JsonResponse({'errors': form.errors}, status=400)
#     else:
#         # For non-POST requests, indicate that only POST is allowed
#         return HttpResponseBadRequest("Only POST requests are allowed for this endpoint.")


