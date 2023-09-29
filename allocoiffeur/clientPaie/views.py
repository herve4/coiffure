from django.shortcuts import render
from payments.models import BasePayment
from django.http import HttpResponse
from clientPaie.models import Paiement
from coiffeurapp.views import *
# class payment(BasePayment):
    
#     def get_failure_url(self)->str:
#         return HttpResponse('commande/{self.pk}/failure/')

# def confirm(request,paiement_id,client_secret):
   

#     paie = Paiement.objects.get(pk=paiement_id)
