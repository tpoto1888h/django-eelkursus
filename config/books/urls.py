from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books, name='books'),
    path('about/', views.about, name='about'),
    path('testing/', views.testing, name='testing'),
    path('available/', views.available, name='available')
]