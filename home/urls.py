from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us/', views.about_us, name='about_us'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('bloopers/', views.bloopers, name='bloopers'),
]
