from django.shortcuts import render
from django.http import HttpResponse


def call_to_action(request):
    return render(request, 'call_to_action.html')
    #return HttpResponse("This is the call to action page")
# Create your views here.
