from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404
from .models import Image, Location, Category
# Create your views here.

def search(request):
    locations = Location.objects.all()
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        images_found = Image.search_image(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{'message':message, 'images':images_found, 'locations':locations})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{'message':message, 'locations':locations})
