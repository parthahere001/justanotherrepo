from django.contrib import admin
from django.urls import path
from quizzer import views

urlpatterns = [
    path('',views.base, name='base'),
    path('home',views.home, name='home'),
    path('register/',views.registration_view, name='register'),
    path('login/',views.login_view, name='login'),
    path('final/',views.finalscore, name='final'),
    path('addquestions/',views.createQuestions, name='addquestions'),
    path('logout',views.logoutUser, name='logout'),
    
]
