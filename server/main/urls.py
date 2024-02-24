# scheduling/urls.py
from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='home_page'),
    path('about/', views.about_page, name='about_page'),
    path('schedule/', views.schedule_page, name='schedule_page'),
    path('march-schedule/', views.march_schedule_page, name='march_schedule'),
    path('april-schedule/', views.april_schedule_page, name='april_schedule'),
    path('coming-soon/', views.coming_soon, name='coming_soon'),
    path('coach-bios/', views.coach_bios, name='coach_bios'),
]
