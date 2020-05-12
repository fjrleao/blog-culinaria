from django.urls import path
from django.conf.urls import url
from blog import views

urlpatterns = [
    path('home/', views.home, name='home')
]