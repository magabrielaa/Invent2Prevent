from django.urls import path
from . import views

urlpatterns = [
    path('', views.call_to_action,name='call_to_action'),
]
