from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signUp, name='signup'),
    path('email_verification/', views.emailVer, name='emailVer'),
    path('loginRater/', views.loginRater, name='loginRater'),
    path('logoutRater/', views.logoutRater, name='logoutRater'),
]