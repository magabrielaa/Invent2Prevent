from django.urls import path

from . import views

urlpatterns = [
    path('', views.research, name='research'),
    path('<int:id>/', views.research, name = 'research'),
    
]

