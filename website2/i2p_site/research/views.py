from django.shortcuts import render
from home.models import Input



def research(request, id=None):
    if(id==None):
        return render(request, '12-15-f-w.html')

    user_input = Input.objects.get(id=id)
    
    #determine the age group user's in
    if(user_input.age=='fill in your info'):
        user_age = 0
    else:
        user_age = user_input.age
        user_gender = user_input.gender.lower()
        user_race = user_input.race.lower()

    if (user_gender=='female'): #for female
        if (user_race=='white'):
            if(user_age == '12-15'):
                file = '12-15-f-w.html'
            elif (user_age == '16-19'):
                file = '16-19-f-w.html'
            elif (user_age == '20-24'):
                file = '20-24-f-w.html'
            elif (user_age == '25-34'):
                file = '25-34-f-w.html'
            elif (user_age == '35-49'):
                file = '35-49-f-w.html'
            elif (user_age == '50-64'):
                file = '50-64-f-w.html'
            else:
                file = '65+-f-w.html'
        elif (user_race=='african american'):
            if(user_age == '12-15'):
                file = '12-15-f-b.html'
            elif (user_age == '16-19'):
                file = '16-19-f-b.html'
            elif (user_age == '20-24'):
                file = '20-24-f-b.html'
            elif (user_age == '25-34'):
                file = '25-34-f-b.html'
            elif (user_age == '35-49'):
                file = '35-49-f-b.html'
            elif (user_age == '50-64'):
                file = '50-64-f-b.html'
            else:
                file = '65+-f-b.html'
        elif (user_race=='hispanic'):
            if(user_age == '12-15'):
                file = '12-15-f-h.html'
            elif (user_age == '16-19'):
                file = '16-19-f-h.html'
            elif (user_age == '20-24'):
                file = '20-24-f-h.html'
            elif (user_age == '25-34'):
                file = '25-34-f-h.html'
            elif (user_age == '35-49'):
                file = '35-49-f-h.html'
            elif (user_age == '50-64'):
                file = '50-64-f-h.html'
            else:
                file = '65+-f-h.html'
        else:
            if(user_age == '12-15'):
                file = '12-15-f-o.html'
            elif (user_age == '16-19'):
                file = '16-19-f-o.html'
            elif (user_age == '20-24'):
                file = '20-24-f-o.html'
            elif (user_age == '25-34'):
                file = '25-34-f-o.html'
            elif (user_age == '35-49'):
                file = '35-49-f-o.html'
            elif (user_age == '50-64'):
                file = '50-64-f-o.html'
            else:
                file = '65+-f-o.html'
    elif ((user_gender=='male') or (user_gender=='man') or (user_gender=='men') or (user_gender=='boy')): #for male
        if (user_race=='white'):
            if(user_age == '12-15'):
                file = '12-15-m-w.html'
            elif (user_age == '16-19'):
                file = '16-19-m-w.html'
            elif (user_age == '20-24'):
                file = '20-24-m-w.html'
            elif (user_age == '25-34'):
                file = '25-34-m-w.html'
            elif (user_age == '35-49'):
                file = '35-49-m-w.html'
            elif (user_age == '50-64'):
                file = '50-64-m-w.html'
            else:
                file = '65+-m-w.html'
        elif (user_race=='african american'):
            if(user_age == '12-15'):
                file = '12-15-m-b.html'
            elif (user_age == '16-19'):
                file = '16-19-m-b.html'
            elif (user_age == '20-24'):
                file = '20-24-m-b.html'
            elif (user_age == '25-34'):
                file = '25-34-m-b.html'
            elif (user_age == '35-49'):
                file = '35-49-m-b.html'
            elif (user_age == '50-64'):
                file = '50-64-m-b.html'
            else:
                file = '65+-m-b.html'
        elif (user_race=='hispanic'):
            if(user_age == '12-15'):
                file = '12-15-m-h.html'
            elif (user_age == '16-19'):
                file = '16-19-m-h.html'
            elif (user_age == '20-24'):
                file = '20-24-m-h.html'
            elif (user_age == '25-34'):
                file = '25-34-m-h.html'
            elif (user_age == '35-49'):
                file = '35-49-m-h.html'
            elif (user_age == '50-64'):
                file = '50-64-m-h.html'
            else:
                file = '65+-m-h.html'
        else:
            if(user_age == '12-15'):
                file = '12-15-m-o.html'
            elif (user_age == '16-19'):
                file = '16-19-m-o.html'
            elif (user_age == '20-24'):
                file = '20-24-m-o.html'
            elif (user_age == '25-34'):
                file = '25-34-m-o.html'
            elif (user_age == '35-49'):
                file = '35-49-m-o.html'
            elif (user_age == '50-64'):
                file = '50-64-m-o.html'
            else:
                file = '65+-m-o.html'  
    else:
        file = 'research.html'

    return render(request, file)


