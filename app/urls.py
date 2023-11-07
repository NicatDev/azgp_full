from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('bloq',blog,name='blog'),
    path('portfolio',portfolio,name='portfolio'),
    path('services',services,name='services'),
    path('contact',contact,name='contact'),
    path('message',message,name='message'),
    path('about',about,name='about'),
    path('bloq/<slug>',blogsingle,name='blogsingle'),
    path('service/<slug>',servicesingle,name='servicesingle'),
    path('portfolio/<slug>',portfoliosingle,name='portfoliosingle'),
]
