from django.urls import path
from . import views

urlpatterns = [
    path('signupBusiness/', views.signupB, name='bsignup'),
    path('email_verification_owner/', views.emailVerB, name='emailVerB'),
    path('adCreate/', views.adCreate, name='adCreate'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('<int:advertisement_pk>/is_done/', views.done, name='done'),


]