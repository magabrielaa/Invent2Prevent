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
        user_age = int(user_input.age)
        user_gender = user_input.gender.lower()
        user_race = user_input.race.lower()

    if ((user_gender=='female') or (user_gender=='woman') or (user_gender=='women') or (user_gender=='girl')): #for female
        if(user_race=='white'):
            if(1<=user_age<=15):
                file = '12-15-f-w.html'
            elif (16<=user_age<=19):
                file = '16-19-f-w.html'
            elif (20<=user_age<=24):
                file = '20-24-f-w.html'
            elif (25<=user_age<=34):
                file = '25-34-f-w.html'
            elif (35<=user_age<=49):
                file = '35-49-f-w.html'
            elif (50<=user_age<=64):
                file = '50-64-f-w.html'
            else:
                file = '65+-f-w.html'
        elif ((user_race=='black') or (user_race=='african american')):
            if(1<=user_age<=15):
                file = '12-15-f-b.html'
            elif (16<=user_age<=19):
                file = '16-19-f-b.html'
            elif (20<=user_age<=24):
                file = '20-24-f-b.html'
            elif (25<=user_age<=34):
                file = '25-34-f-b.html'
            elif (35<=user_age<=49):
                file = '35-49-f-b.html'
            elif (50<=user_age<=64):
                file = '50-64-f-b.html'
            else:
                file = '65+-f-b.html'
        else:
            if(1<=user_age<=15):
                file = '12-15-f-h.html'
            elif (16<=user_age<=19):
                file = '16-19-f-h.html'
            elif (20<=user_age<=24):
                file = '20-24-f-h.html'
            elif (25<=user_age<=34):
                file = '25-34-f-h.html'
            elif (35<=user_age<=49):
                file = '35-49-f-h.html'
            elif (50<=user_age<=64):
                file = '50-64-f-h.html'
            else:
                file = '65+-f-h.html'  
    elif ((user_gender=='male') or (user_gender=='man') or (user_gender=='men') or (user_gender=='boy')): #for male
        if(user_race=='white'):
            if(1<=user_age<=15):
                file = '12-15-m-w.html'
            elif (16<=user_age<=19):
                file = '16-19-m-w.html'
            elif (20<=user_age<=24):
                file = '20-24-m-w.html'
            elif (25<=user_age<=34):
                file = '25-34-m-w.html'
            elif (35<=user_age<=49):
                file = '35-49-m-w.html'
            elif (50<=user_age<=64):
                file = '50-64-m-w.html'
            else:
                file = '65+-m-w.html'
        elif ((user_race=='black') or (user_race=='african american')):
            if(1<=user_age<=15):
                file = '12-15-m-b.html'
            elif (16<=user_age<=19):
                file = '16-19-m-b.html'
            elif (20<=user_age<=24):
                file = '20-24-m-b.html'
            elif (25<=user_age<=34):
                file = '25-34-m-b.html'
            elif (35<=user_age<=49):
                file = '35-49-m-b.html'
            elif (50<=user_age<=64):
                file = '50-64-m-b.html'
            else:
                file = '65+-m-b.html'
        else:
            if(1<=user_age<=15):
                file = '12-15-m-h.html'
            elif (16<=user_age<=19):
                file = '16-19-m-h.html'
            elif (20<=user_age<=24):
                file = '20-24-m-h.html'
            elif (25<=user_age<=34):
                file = '25-34-m-h.html'
            elif (35<=user_age<=49):
                file = '35-49-m-h.html'
            elif (50<=user_age<=64):
                file = '50-64-m-h.html'
            else:
                file = '65+-m-h.html'  
    else:
        file = 'research.html'

    return render(request, file)


