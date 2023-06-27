from django.urls import path
from initial import views

app_name = 'initial'

urlpatterns = [
    path('', views.initial, name='initial'),
    path('books/create', views.createBook, name='book_create')
]