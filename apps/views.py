from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def users(request):
    return render(request, 'users.html')

def types(request):
    return render(request, 'types.html')

def places(request):
    return render(request, 'places.html')

def reviews(request):
    return render(request, 'reviews.html')
def favorites(request):
    return render(request, 'favorites.html')

def services(request):
    return render(request, 'services.html')

def banners(request):
    return render(request, 'banners.html')

def cities(request):
    return render(request, 'cities.html')

def upload(request):
    return render(request, 'upload.html')

def settings(request):
    return render(request, 'settings.html')


def pages_calendar(request):
    return render(request, 'pages-calendar.html')
def pages_pricing(request):
    return render(request, 'pages-pricing.html')
def pages_faqs(request):
    return render(request, 'pages-faqs.html')
def auth_lock_screen(request):
     return render(request, 'auth-lock-screen.html')

def auth_signin(request):
    return render(request, 'auth-signin.html')