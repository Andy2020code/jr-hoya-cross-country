# scheduling/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('about/', views.about_page, name='about_page'),
    path('schedule/', views.schedule_page, name='schedule_page')
]
