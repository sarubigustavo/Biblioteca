from django.urls import path
from initial import views

urlpatterns = [
    path('', views.initial, name='initial')
]