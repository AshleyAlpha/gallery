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
    return render(request, 'index.html', {'title':title, 'images':images, 'locations':locations})

def search(request):
    locations = Location.objects.all()
    if 'category' in request.GET and request.GET['category']:
        search_category = request.GET.get('category')
        images = Image.search_image(search_category)
        message = f'{search_category}

        return render(request, 'search.html',{'message':message, 'images':images, 'locations':locations})
    else:
        message = "You have not searched for any term"
        return render(request, 'search.html',{'message':message,'locations':locations})

def sing_image(request,image_id):

    image = Image.objects.get(id=image_id)
    return render(request, 'sing_image.html',{'image':image})

def location_filter(request, location_id):
    try:
        location = Location.objects.get(id = location_id)
        images = Image.objects.filter(location = location.id)
    except:
        raise Http404()
    return render(request,'location.html',{'location':location,'images':images})
