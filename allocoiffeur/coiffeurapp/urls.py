from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from coiffeurapp.views import *




urlpatterns = [
    path('coiffures/',views.coiffures,name='coiffures'),
    path('galeries/',galeries,name='galeries'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


