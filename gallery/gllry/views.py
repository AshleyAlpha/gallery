from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404
from .models import Image, Location, Category
# Create your views here.

def welcome(request):
    return render(request, 'Welcome.html')

def index(request):
    title = 'Home'
    images = Image.objects.all()
    locations = Location.objects.all()
    return render(request, 'all-pics/index.html', {'title':title, 'images':images, 'locations':locations})

def search(request):
    locations = Location.objects.all()
    if 'category' in request.GET and request.GET['category']:
        search_category = request.GET.get('category')
        images = Image.search_image(search_category)
        message = f'{search_category}'

        return render(request, 'search.html',{'message':message, 'images':images, 'locations':locations})
    else:
        message = "You have not searched for any term"
        return render(request, 'all-pics/search.html',{'message':message,'locations':locations})

# def sing_image(request, category_name, image_id):
#     locations = Location.objects.all()
#     image = Image.get_image_by_id(image_id)
#     image_category = Image.objects.filter(category__photo_category = category_name)
#     title = f'{category_name}'
#     return render(request, 'location.html', {'title':title, 'images':images, 'locations':locations})

def location_filter(request, location):
    locations = Location.objects.all()
    images = Image.filter_by_location(location)
    title = f'{location} Photos'
    return render(request, 'all-pics/location.html', {'title':title, 'images':images, 'locations':locations})
