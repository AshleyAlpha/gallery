from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name='home'),
    url(r'^search/',views.search,name = 'search'),
    url(r'^image/(\d+)',views.sing_image,name = 'picture'), 
     url(r'^location/(\d+)',views.location_filter,name = 'showlocation') 
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)