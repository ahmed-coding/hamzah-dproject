from django.shortcuts import render, redirect, get_object_or_404
from firebase_admin import firestore
from datetime import datetime
import json

db = firestore.client()

def index(request):
    # Fetch data from 'Banner_city' collection
    banner_city_ref = db.collection('Banner_city')
    docs = banner_city_ref.get()
    data = {}
    # Get All the documents data
    for doc in docs:
        data[doc.id] = doc.to_dict()

     # Initialize counts to zero
    new_users = 0
    new_reviews = 0
    new_places = 0
    total_cities = 0

    # Fetch the count from database
    users_ref = db.collection('Users').get()
    new_users = len(users_ref)
    reviews_ref = db.collection('User_comments').get()
    new_reviews = len(reviews_ref)
    places_ref = db.collection('Places').get()
    new_places = len(places_ref)
    cities_ref = db.collection('Citys').get()
    total_cities = len(cities_ref)



    context = {
        'banner_city_data': data,
          'new_users': new_users,
        'new_reviews': new_reviews,
        'new_places': new_places,
        'total_cities': total_cities,
    }
    return render(request, 'index.html', context)


def banners(request):
    # Fetch all banner data from firebase
    banner_ref = db.collection('Banners')
    docs = banner_ref.get()
    banners_data = []
    for doc in docs:
        banner_data = doc.to_dict()

        # Fetch City Name
        city_id = banner_data.get('city_id')
        city_name = "Unknown"  # Default value
        if city_id:
            city_ref = db.collection('Citys').document(str(city_id)).get()
            if city_ref.exists:
                city_name = city_ref.to_dict().get('name', "Unknown")
        # Fetch Category Name
        category_id = banner_data.get('category')
        category_name = "Unknown"  # Default value
        if category_id:
            category_ref = db.collection('Places_type').document(str(category_id)).get()
            if category_ref.exists:
                category_name = category_ref.to_dict().get('type_name', "Unknown")


        banners_data.append({
            'id': doc.id,
            'data': banner_data,
            'city_name': city_name,
             'category_name': category_name,
        })
    return render(request, 'banners.html', {'banners_data': banners_data})

def create_banner(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.POST.get('image')
        category = int(request.POST.get('category'))
        city_id = int(request.POST.get('city_id'))
        is_active = request.POST.get('is_active') == 'on'
        start_time = int(request.POST.get('start_time'))
        end_time = int(request.POST.get('end_time'))
        time_created = int(datetime.now().timestamp())
        # Create the new document and the corresponding data for that document
        doc_ref = db.collection('Banners').document()
        doc_ref.set({
            'title': title,
            'description': description,
            'image': image,
            'category': category,
            'city_id': city_id,
            'is_active': is_active,
            'start_time': start_time,
            'end_time': end_time,
            'time_created': time_created,
            'id': int(doc_ref.id, 16)
        })
        return redirect('banners')

    # Fetch city options for dropdown
    citys_ref = db.collection('Citys')
    citys_docs = citys_ref.get()
    citys = []
    for doc in citys_docs:
        citys.append({'id': doc.id, 'name': doc.to_dict().get('city_name')})
     # Fetch types options for dropdown
    types_ref = db.collection('Types')
    types_docs = types_ref.get()
    types = []
    for doc in types_docs:
        types.append({'id': doc.id, 'name': doc.to_dict().get('name')})
    return render(request, 'create_banner.html', {'citys': citys, 'types': types})



def users(request):
    # Fetch user data from firebase
    users_ref = db.collection('Users')
    docs = users_ref.get()
    users_data = []
    for doc in docs:
        users_data.append({ 'id': doc.id, 'data': doc.to_dict() })
    return render(request, 'users.html', {'users_data': users_data})

def create_user(request):
      if request.method == 'POST':
           user_name = request.POST.get('user_name')
           user_email = request.POST.get('user_email')
           user_password = request.POST.get('user_password')
           user_image = request.POST.get('user_image')
           user_created_at = str(datetime.now())
        # Create the new document and the corresponding data for that document
           doc_ref = db.collection('Users').document()
           doc_ref.set({
                'user_name': user_name,
                'user_email': user_email,
                'user_password': user_password,
                'user_image': user_image,
                'user_created_at': user_created_at,
                'user_id': doc_ref.id
           })
           return redirect('users')
      return render(request, 'create_user.html')
  



def reviews(request):
    # Fetch user comments data from firebase
    reviews_ref = db.collection('User_comments')
    docs = reviews_ref.get()
    reviews_data = []
    for doc in docs:
        review_data = doc.to_dict()
        # Fetch User name
        user_id = review_data.get('user_id')
        user_name = "Unknown"
        if user_id:
             user_ref = db.collection('Users').document(str(user_id)).get()
             if user_ref.exists:
                 user_name = user_ref.to_dict().get('user_name', 'Unknown')
         # Fetch Place Name
        place_id = review_data.get('place_id')
        place_name = "Unknown"
        if place_id:
           place_ref = db.collection('Places').document(str(place_id)).get()
           if place_ref.exists:
               place_name = place_ref.to_dict().get('name', 'Unknown')

        reviews_data.append({
            'id': doc.id,
            'data': review_data,
            'user_name': user_name,
             'place_name': place_name,
        })
    return render(request, 'reviews.html', {'reviews_data': reviews_data})


def create_review(request):
    if request.method == 'POST':
           message = request.POST.get('message')
           place_id = int(request.POST.get('place_id'))
           rate = int(request.POST.get('rate'))
           user_id = int(request.POST.get('user_id'))
           user_image = request.POST.get('user_image')
           user_name = request.POST.get('user_name')
           timestamp = str(datetime.now())

        # Create the new document and the corresponding data for that document
           doc_ref = db.collection('User_comments').document()
           doc_ref.set({
               'message': message,
               'place_id': place_id,
               'rate': rate,
               'timestamp': timestamp,
               'user_id': user_id,
              'user_image': user_image,
              'user_name': user_name
           })
           return redirect('reviews')

    # Fetch city options for dropdown
    users_ref = db.collection('Users')
    users_docs = users_ref.get()
    users = []
    for doc in users_docs:
       users.append({'id': doc.id, 'name': doc.to_dict().get('user_name')})
    # Fetch types options for dropdown
    places_ref = db.collection('Places')
    places_docs = places_ref.get()
    places = []
    for doc in places_docs:
        places.append({'id': doc.id, 'name': doc.to_dict().get('name')})
    return render(request, 'create_review.html', {'users': users, 'places': places})


def places(request):
    # Fetch places data from firebase
    places_ref = db.collection('Places')
    docs = places_ref.get()
    places_data = []
    for doc in docs:
         place_data = doc.to_dict()
          # Fetch City Name
         city_id = place_data.get('city_id')
         city_name = "Unknown"  # Default value
         if city_id:
              city_ref = db.collection('Citys').document(str(city_id)).get()
              if city_ref.exists:
                  city_name = city_ref.to_dict().get('city_name', "Unknown")

          # Fetch Type Name
         type_id = place_data.get('type_id')
         type_name = "Unknown"  # Default value
         if type_id:
              type_ref = db.collection('Places_type').document(str(type_id)).get()
              if type_ref.exists:
                  type_name = type_ref.to_dict().get('type_name', "Unknown")


         places_data.append({
            'id': doc.id,
            'data': place_data,
             'city_name': city_name,
             'type_name': type_name
        })
    return render(request, 'places.html', {'places_data': places_data})

def create_place(request):
     if request.method == 'POST':
          place_name = request.POST.get('place_name')
          place_description = request.POST.get('place_description')
          place_location = request.POST.get('place_location')
          place_latitude = request.POST.get('place_latitude')
          place_longitude = request.POST.get('place_longitude')
          place_image = request.POST.get('place_image')
          city_id = request.POST.get('city_id')
          type_id = request.POST.get('type_id')
          rate_avg = request.POST.get('rate_avg')
          review_num = int(request.POST.get('review_num'))
         # Create the new document and the corresponding data for that document
          doc_ref = db.collection('Places').document()
          doc_ref.set({
            'place_name': place_name,
            'place_description': place_description,
            'place_location': place_location,
            'place_latitude': place_latitude,
            'place_longitude': place_longitude,
            'place_image': place_image,
            'city_id': city_id,
            'type_id': type_id,
            'rate_avg': rate_avg,
            'review_num': review_num,
             'place_id': doc_ref.id
          })
          return redirect('places')

    # Fetch city options for dropdown
     citys_ref = db.collection('Citys')
     citys_docs = citys_ref.get()
     citys = []
     for doc in citys_docs:
        citys.append({'id': doc.id, 'name': doc.to_dict().get('city_name')})

    # Fetch types options for dropdown
     types_ref = db.collection('Places_type')
     types_docs = types_ref.get()
     types = []
     for doc in types_docs:
        types.append({'id': doc.id, 'name': doc.to_dict().get('type_name')})


     return render(request, 'create_place.html',{'citys': citys, 'types': types})


def update_place(request, place_id):
    place_ref = db.collection('Places').document(place_id).get()
    if not place_ref.exists:
       return render(request, 'not_found.html')

    if request.method == 'POST':
         place_name = request.POST.get('place_name')
         place_description = request.POST.get('place_description')
         place_location = request.POST.get('place_location')
         place_latitude = request.POST.get('place_latitude')
         place_longitude = request.POST.get('place_longitude')
         place_image = request.POST.get('place_image')
         city_id = request.POST.get('city_id')
         type_id = request.POST.get('type_id')
         rate_avg = request.POST.get('rate_avg')
         review_num = int(request.POST.get('review_num'))

        # Create the new document and the corresponding data for that document
         doc_ref = db.collection('Places').document(place_id)
         doc_ref.update({
            'place_name': place_name,
            'place_description': place_description,
            'place_location': place_location,
            'place_latitude': place_latitude,
            'place_longitude': place_longitude,
             'place_image': place_image,
            'city_id': city_id,
            'type_id': type_id,
            'rate_avg': rate_avg,
             'review_num': review_num
         })
         return redirect('places')

   # Fetch city options for dropdown
    citys_ref = db.collection('Citys')
    citys_docs = citys_ref.get()
    citys = []
    for doc in citys_docs:
       citys.append({'id': doc.id, 'name': doc.to_dict().get('city_name')})
   # Fetch types options for dropdown
    types_ref = db.collection('Places_type')
    types_docs = types_ref.get()
    types = []
    for doc in types_docs:
       types.append({'id': doc.id, 'name': doc.to_dict().get('type_name')})

    return render(request, 'update_place.html', {'place': place_ref.to_dict(), 'place_id':place_id,  'citys': citys, 'types': types})


def types(request):
    # Fetch places type data from firebase
    types_ref = db.collection('Places_type')
    docs = types_ref.get()
    types_data = []
    for doc in docs:
         types_data.append({ 'id': doc.id, 'data': doc.to_dict() })
    return render(request, 'types.html', {'types_data': types_data})

def create_type(request):
    if request.method == 'POST':
         type_name = request.POST.get('type_name')
         type_icon = request.POST.get('type_icon')

        # Create the new document and the corresponding data for that document
         doc_ref = db.collection('Places_type').document()
         doc_ref.set({
            'type_name': type_name,
            'type_icon': type_icon,
            'type_id':  doc_ref.id
         })
         return redirect('types')
    return render(request, 'create_type.html')


def update_type(request, type_id):
    type_ref = db.collection('Places_type').document(type_id).get()
    if not type_ref.exists:
       return render(request, 'not_found.html')


    if request.method == 'POST':
         type_name = request.POST.get('type_name')
         type_icon = request.POST.get('type_icon')

        # Create the new document and the corresponding data for that document
         doc_ref = db.collection('Places_type').document(type_id)
         doc_ref.update({
             'type_name': type_name,
             'type_icon': type_icon
         })
         return redirect('types')
    return render(request, 'update_type.html', {'type': type_ref.to_dict(), 'type_id':type_id })



def upload(request):
     if request.method == 'POST' and request.FILES.get('places_file'):
        places_file = request.FILES['places_file']
        try:
              # Decode the bytes to string and then convert the json string to a dict
            file_content = places_file.read().decode('utf-8')
            data = json.loads(file_content)
             # Use the list of dictionary to save data on firestore
            for place in data:
                doc_ref = db.collection('Places').document()
                place['place_id'] = doc_ref.id
                doc_ref.set(place)
        except Exception as e:
           # you may add logging system here
           print(f"Error processing file: {e}")
           return render(request, 'upload.html', {'error': f"Error processing file: {e}"})

        return render(request, 'upload.html', {'message': 'Places file uploaded successfully'})
     return render(request, 'upload.html')



def places_images(request):
     # Fetch places images data from firebase
    images_ref = db.collection('Places_images')
    docs = images_ref.get()
    images_data = []
    for doc in docs:
         images_data.append({ 'id': doc.id, 'data': doc.to_dict() })
    return render(request, 'places_images.html', {'images_data': images_data})


def create_place_image(request):
    if request.method == 'POST':
         image = request.POST.get('image')
         place_id = request.POST.get('place_id')
        # Create the new document and the corresponding data for that document
         doc_ref = db.collection('Places_images').document()
         doc_ref.set({
            'image': image,
             'place_id': place_id,
            'image_id': doc_ref.id
         })
         return redirect('places_images')
    # Fetch all of the places to select from in the form
    places_ref = db.collection('Places')
    places_docs = places_ref.get()
    places = []
    for doc in places_docs:
       places.append({'id': doc.id, 'name': doc.to_dict().get('place_name')})
    return render(request, 'create_place_image.html', {'places': places})


def update_place_image(request, image_id):
    image_ref = db.collection('Places_images').document(image_id).get()
    if not image_ref.exists:
       return render(request, 'not_found.html')
    if request.method == 'POST':
         image = request.POST.get('image')
         place_id = request.POST.get('place_id')
        # Create the new document and the corresponding data for that document
         doc_ref = db.collection('Places_images').document(image_id)
         doc_ref.update({
            'image': image,
              'place_id': place_id
         })
         return redirect('places_images')
       # Fetch all of the places to select from in the form
    places_ref = db.collection('Places')
    places_docs = places_ref.get()
    places = []
    for doc in places_docs:
       places.append({'id': doc.id, 'name': doc.to_dict().get('place_name')})

    return render(request, 'update_place_image.html', {'image': image_ref.to_dict(), 'image_id': image_id, 'places': places })


def favorites(request):
    return render(request, 'favorites.html')

def services(request):
    return render(request, 'services.html')


def cities(request):
    return render(request, 'cities.html')


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