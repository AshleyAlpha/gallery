from django.conf.urls import url
from . import views

urlpatterns=[
    url('^/$',views.index,name='home'),
    url(r'^search/$',views.search,name = 'search_pics') 
]
