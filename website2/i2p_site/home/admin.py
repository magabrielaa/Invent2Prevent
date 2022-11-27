from django.contrib import admin
from home.models import Input

class InputAdmin(admin.ModelAdmin):
   list_display = ('race', 'gender', 'age') 

admin.site.register(Input, InputAdmin)
# Register your models here.
