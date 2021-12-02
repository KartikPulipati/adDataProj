from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signUp, name='signup'),
    path('email_verification/', views.emailVer, name='emailVer'),
    path('loginUser/', views.loginRater, name='loginRater'),
    path('logoutUser/', views.logoutRater, name='logoutRater'),
    path('discover/', views.discover, name='discover'),
    path('<int:advertisement_pk>/view', views.viewAd, name='viewAd'),
]