"""
URL configuration for allocoiffeur project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls import  include
from django.urls import re_path 
from rest_framework import routers
from django.conf.urls.static import static
from coiffeurapp.views import *
from coiffuresapp.views import *
from auth_coiffeur.views import *
from commandeapp.views import *
from django.contrib.auth.decorators import login_required
from auth_coiffeur.views import *




urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^inscription/$',creation,name='inscription'),
    re_path(r'^login/$',loginAuthview.as_view(),name='login'),
    re_path(r'^logout/$',logoutView.as_view(),name='logout'),
    path('confirm/<pk>/',confirm.as_view(),name='confirm'),
    path('',include('coiffuresapp.urls')),
    path('',include('auth_coiffeur.urls')),
    path('404/',page404,name='nofound'),
    path('coiffures/',coiffures,name='coiffures'),
    path('actualites/',actualites,name='actualites'),
    path('coiffure/',coiffure,name='coiffure'),
    path('categories/<str:pk>',galeries,name='galeries'),
    path('contact/',contact,name='contact'),
    path('contacts/',contacts,name='contacts'),
    path('coiffures/search/',search,name='search'),
    path('<slug:coiffure_slug>/',show,name='show'),
    path('choix/',choix,name='choix'),
    path('commande/<slug:coiffure_slug>',commande,name='commande'),
    
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)



