from django.urls import path
from . import views

urlpatterns = [
    path('register_business/', views.register_business, name='register_business'),
]