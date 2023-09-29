from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import coiffuresapp
from django.conf.urls import handler404


urlpatterns = [
    path('',coiffuresapp,name='coiffuresapp'),
  
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

# handler404 ='coiffuresapp.views.page404'
