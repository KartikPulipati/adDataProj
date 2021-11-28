from django.urls import path
from . import views

urlpatterns = [
    path('signupBusiness/', views.signupB, name="bsignup"),
    path('email_verification_owner/', views.emailVer, name='emailVerB'),
    path('adCreate/', views.adCreate, name='adCreate'),


]