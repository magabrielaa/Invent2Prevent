from django import forms
from home.models import Input



class InputYourInfoForm(forms.ModelForm):
   class Meta:
     model = Input
     fields = '__all__'

