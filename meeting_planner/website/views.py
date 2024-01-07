from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

from meetings.models import Meeting

# Create your views here.
def welcome(request):
    return render(request, "website/welcome.html",
        {"num_meetings": Meeting.objects.count()})
    #    {"message": "This data was sent from the view to the template."})
    # return HttpResponse("Welcome to the Meeting Planner")

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))

def about(request):
    MyAbout = "Hello, my name is El Guapo.  I am a HAM radio enthusiast"
    return HttpResponse(MyAbout)


