
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inputs/<int:id>/', views.input_detail, name = 'input-detail'),
]

