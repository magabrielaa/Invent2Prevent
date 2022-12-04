from django.http import HttpResponse
from django.shortcuts import render
from home.models import Input
from home.forms import InputYourInfoForm
from django.shortcuts import redirect

def home(request):
    size = len(Input.objects.all())
    latest_input = Input.objects.all()[(size-1)]

    form = InputYourInfoForm()

    if request.method == 'POST':
        form = InputYourInfoForm(request.POST)
        if form.is_valid():
            i = form.save()
            return redirect('research', i.id)
    else:
        form = InputYourInfoForm()

    return render(request, 'home.html', {'form': form, 'latest_input': latest_input})
    #return HttpResponse("This is the home page")



def input_detail(request, id):  # note the additional id parameter
    user_input = Input.objects.get(id=id)
    return render(request, 'input_detail.html', {'user_input': user_input})
