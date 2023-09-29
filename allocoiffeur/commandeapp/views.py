from django.shortcuts import render
from coiffuresapp.forms import clientForm
from coiffuresapp.models import *
from django.contrib import messages
from django.shortcuts import redirect,get_object_or_404
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import permission_required
import stripe
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import json
from django.views.generic import TemplateView
from random import random,randint, randrange



def commande(request,coiffure_slug):
    
    coi = coiffuresGaleries.objects.get(slugs=coiffure_slug)
    if coiffuresGaleries.objects.filter(slugs=coi).exists() is None:
        return redirect('nofound')
  
    context = {'coi':coi}

    if request.method == 'POST':
        
        try:
            nom = request.POST.get('nom')
            email = request.POST.get('email')
            tel = request.POST.get('tel')
            adresse = request.POST.get('adresse')
            datecoi = request.POST.get('date')
            heure = request.POST.get('heure')
            # stripe = request.POST.get('stripe')
            # paypal = request.POST.get('paypal')
            paie = request.POST.get('paie')
        
            if client.objects.all().filter(telephone_cl=tel).exists():
                messages.error(request,"Ce numéro existe déjà !")
                return render(request,'validation/validation.html',context)
            elif client.objects.all().filter(email_cl=email).exists():
                messages.error(request,"Cet email existe déjà !")
                return render(request,'validation/validation.html',context)
            elif paie is None:
                messages.error(request,"Veuillez remplir tous les champs !")
                return render(request,'validation/validation.html',context)
            else:
                
                cl = client(
                                nom_cl = nom,
                                email_cl=email,
                                telephone_cl=tel,
                                adresse_cl=adresse,
                                montant=coi.prix_coi,
                                time_coi=heure,
                                days_coi=datecoi,
                                secret=randrange(1,999999),
                                paie=paie,
                                coiffure=coi    
                                )
                cl.save()
                
                # title = '#Réservation confirmée'
                # img = '<div> <img src="{{coi.img_coi.url}}" width="100px" height="auto"></div>'
                # message = f'Bravo {cl.nom_cl} ! \n Vous avez réservé un coiffeur pour {cl.days_coi} à {cl.time_coi} \n - Coupe : {coi.nom_coi}\n - Prix : {coi.prix_coi}\n ',img
                # hostUser = 'settings.EMAIL_HOST_USER'
                # send_mail(title,message,hostUser,[cl.email_cl],fail_silently=False)
                        
                messages.success(request,"Votre réservation est prise en compte !")
                return render(request,'validation/validation.html',context)
        except:
            messages.error(request,"Pour commander un(e) autre coiffeur(se), inscrivez-vous pour une meilleure expérience !")
            return render(request,'validation/validation.html',context)
 
    return render(request,'validation/validation.html',context)
                
   
   
        



# def confirm(request,**kwargs):
#     return render(request,'validation/confirm.html',**kwargs)




# stripe.api_key = settings.STRIPE_SECRET_KEY 
# app = Flask(__name__,
#                     static_url_path='',
#                     static_folder='public')

# YOUR_DOMAIN = '/confirm/'
# class confirm(View):
#     @app.route('confirm/', methods=['POST'])
#     def post(self,request,*args,**kwargs):
#         coiffure_id = self.kwargs['pk']
#         client_id = self.kwargs['pk']
#         coi = coiffuresGaleries.objects.get(pk=coiffure_id)
#         clien = client.get_object_or_404(pk=client_id)

#         try:
#             checkout_session = stripe.checkout.Session.create(
#                 payment_method_types=['card'],
#                 line_items=[
#                     {
#                         # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
#                         ''
#                         'Coiffure': {{coi.nom_coi}},
#                         'Prix': {{coi.prix_coi}},
#                         'Client': {{clien.nom_cl}},
                        
#                     },
#                 ],
#                 mode='payment',
#                 success_url=YOUR_DOMAIN + '/success',
#                 cancel_url=YOUR_DOMAIN + '/cancel',
#             )
#         except Exception as e:
#             return str(e)

#         return redirect(checkout_session.url, code=303)

#     if __name__ == '__main__':
#         app.run(port=8000)
    # def create_checkout_session():


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"   


class confirm(View):
    template_name = "validation/confirm.html" 
    def post(self, request, *args, **kwargs):
        try:
            req_json = json.loads(request.body)
            clien = stripe.Customer.create(email=req_json['email'])
            clien = self.kwargs['pk']
            cl = client.objects.get(id=clien)
            coiffure_id = self.kwargs["pk"]
            coi = coiffuresGaleries.objects.get(id=coiffure_id)
            intent = stripe.PaymentIntent.create(
                amount=coi.prix_coi,
                currency='usd',
                customer=clien['pk'],
                metadata={
                    "Nom client": cl.nom_cl
                },
              
            )
            return JsonResponse({
                'clientSecret': intent['client_secret']
            })
        except Exception as e:
            return JsonResponse({ 'error': str(e) })