from django.conf.urls import  include
from django.urls import re_path ,path
from rest_framework import routers
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',auth_coiffeur,name='auth_coiffeur'),
   
]
