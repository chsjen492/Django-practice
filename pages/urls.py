from django.urls import path

from . import views

urlpatterns = [
    path('', views.mainpage),
    path('company/', views.company),
    path('services/', views.services),
    path('promotion/', views.promotion),
    path('contact/', views.contact),
    path('recruit/', views.recruit),
    path('services/1', views.service1),
]
