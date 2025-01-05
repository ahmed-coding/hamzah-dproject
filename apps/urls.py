from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.users, name='users'),
    path('types/', views.types, name='types'),
    path('places/', views.places, name='places'),
    path('reviews/', views.reviews, name='reviews'),
    path('favorites/', views.favorites, name='favorites'),
    path('services/', views.services, name='services'),
    path('banners/', views.banners, name='banners'),
    path('cities/', views.cities, name='cities'),
    path('upload/', views.upload, name='upload'),
     path('settings/', views.settings, name='settings'),


    path('pages-calendar/', views.pages_calendar, name='pages-calendar'),
    path('pages-pricing/', views.pages_pricing, name='pages-pricing'),
    path('pages-faqs/', views.pages_faqs, name='pages-faqs'),
    path('auth-lock-screen/', views.auth_lock_screen, name='auth-lock-screen'),
     path('auth-signin/', views.auth_signin, name='auth-signin'),
]