from django.urls import path
from commandeapp.views import commande

urlpatterns = [
    path('',commande,name='commande'),
]
