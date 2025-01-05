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
     path('cities/create/', views.create_city, name='create_city'), # Add create city urls
    path('cities/update/<str:city_id>/', views.update_city, name='update_city'), # Add update city urls
    path('countries/', views.countries, name='countries'), # Add country urls
    path('countries/create/', views.create_country, name='create_country'), # Add create country urls
    path('countries/update/<str:country_id>/', views.update_country, name='update_country'), # Add update country urls
    path('upload/', views.upload, name='upload'),
    path('settings/', views.settings, name='settings'),
    path('banners/create/', views.create_banner, name='create_banner'), # Add create banner urls
    path('users/create/', views.create_user, name='create_user'), # Add create user urls
    path('reviews/create/', views.create_review, name='create_review'), # Add create review urls
    path('places/create/', views.create_place, name='create_place'), # Add create place urls
    path('places/update/<str:place_id>/', views.update_place, name='update_place'), # Add update place urls
    path('types/create/', views.create_type, name='create_type'), # Add create type urls
     path('types/update/<str:type_id>/', views.update_type, name='update_type'), # Add update type urls

    path('places_images/', views.places_images, name='places_images'), # Add places images urls
    path('places_images/create/', views.create_place_image, name='create_place_image'), # Add create places images urls
     path('places_images/update/<str:image_id>/', views.update_place_image, name='update_place_image'), # Add update places images urls


    path('services/', views.services, name='services'), # Add services urls
    path('services/create/', views.create_service, name='create_service'), # Add create services urls
     path('services/update/<str:service_id>/', views.update_service, name='update_service'), # Add update services urls
    path('places_services/', views.places_services, name='places_services'), # Add places services urls
    path('places_services/create/', views.create_place_service, name='create_place_service'), # Add create places services urls
    path('places_services/update/<str:place_service_id>/', views.update_place_service, name='update_place_service'), # Add update places services urls



    path('pages-calendar/', views.pages_calendar, name='pages-calendar'),
    path('pages-pricing/', views.pages_pricing, name='pages-pricing'),
    path('pages-faqs/', views.pages_faqs, name='pages-faqs'),
    path('auth-lock-screen/', views.auth_lock_screen, name='auth-lock-screen'),
     path('auth-signin/', views.auth_signin, name='auth-signin'),
]