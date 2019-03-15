from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'bienvenue'),
    url('^today/$',views.pics_of_day,name='picsToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.prev_days_pics,name = 'lastPics') 
]
