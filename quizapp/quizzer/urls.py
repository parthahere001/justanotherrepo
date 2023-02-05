from django.contrib import admin
from django.urls import path
from quizzer import views

urlpatterns = [
    path('',views.home, name='home'),
    path('register/',views.registration_view, name='register'),
    path('login/',views.login_view, name='login'),
]
