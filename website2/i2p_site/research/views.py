from django.shortcuts import render
from home.models import Input



def research(request, id=None):
    if(id==None):
        return render(request, 'research.html')
    user_input = Input.objects.get(id=id)
    return render(request, 'research.html', {'user_input': user_input})

