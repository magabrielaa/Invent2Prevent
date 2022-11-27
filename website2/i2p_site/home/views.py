from django.http import HttpResponse
from django.shortcuts import render
from home.models import Input
from home.forms import InputYourInfoForm
from django.core.mail import send_mail
from django.shortcuts import redirect

def home(request):
    size = len(Input.objects.all())
    latest_input = Input.objects.all()[(size-1)]

    form = InputYourInfoForm()

    if request.method == 'POST':
        form = InputYourInfoForm(request.POST)
    else:
        form = InputYourInfoForm()

    return render(request, 'home.html', {'form': form, 'latest_input': latest_input})
    #return HttpResponse("This is the home page")



def input_detail(request, id):  # note the additional id parameter
    return render(request, 'templates/input_detail.html', {'id':id})
