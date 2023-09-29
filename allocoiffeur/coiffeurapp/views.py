from django.shortcuts import render
from urllib3 import HTTPResponse
from coiffuresapp.models import categorisCoiffures,client, coiffuresGaleries, Contacts
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import redirect
import verify_email
from random import random,randint, randrange
from django.db.models import Q

datalist = categorisCoiffures.objects.all().filter(Q(nom_cat="Maquillage")|Q(nom_cat="Ongléries"))
barbe = categorisCoiffures.objects.all().filter(nom_cat="Barbes")

def coiffures(request):
    page = 'coiffures'
    
    hommes = coiffuresGaleries.objects.filter(coiffurePour__name='Hommes')
    femmes = coiffuresGaleries.objects.filter(coiffurePour__name='Femmes')
    
 
    context = {
                'datalist':datalist,
                'hommes':hommes,
                'femmes':femmes,
                'page':page,
                'barbe':barbe,
                }
    return render(request,'coiffures.html',context)
def coiffure(req):
    page = 'coiffure'
    
    hommes = coiffuresGaleries.objects.filter(coiffurePour__name='Hommes')
    femmes = coiffuresGaleries.objects.filter(coiffurePour__name='Femmes')
    
 
    context = {
                'datalist':datalist,
                'hommes':hommes,
                'femmes':femmes,
                'page':page,
                'barbe':barbe,
                }
    return render(req,'coiffures.html',context)
def actualites(req):
    return render(req,'actualites.html')
def galeries(request,pk):
    page = 'galeries'
    categories = categorisCoiffures.objects.get(nom_cat=pk)
    hommes = categories.coiffuresgaleries_set.filter(coiffurePour__name='Hommes')
    femmes = categories.coiffuresgaleries_set.filter(coiffurePour__name='Femmes')
    data = categories.coiffuresgaleries_set.all()
    data2 = categorisCoiffures.objects.filter(coiffurePour__name='Hommes').distinct()
    data3 =categorisCoiffures.objects.filter(coiffurePour__name='Femmes').distinct()
 
    pages = Paginator(data, 6)
    page_list = request.GET.get('pages')
    pages = pages.get_page(page_list)
    listCoi = {
        'pages':pages,
        'hommes':hommes,
        'femmes':femmes ,
        'categories':categories,
        'page':page,
        'data2':data2,
        'data3':data3,
    }
    return render(request,'galeries.html',listCoi)

def show(request,coiffure_slug):
    data = coiffuresGaleries.objects.get(slugs=coiffure_slug)
    if coiffuresGaleries.objects.filter(slugs=data).exists() is None:
        return redirect('nofound')
    
  
    
   
    tout = coiffuresGaleries.objects.filter(categorieCoiffures__nom_cat__icontains=data.categorieCoiffures.nom_cat)[2:]
    page = Paginator(tout,randrange(1, 100))
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    aff = {'page':page,'data':data}
    return render(request,'show.html',aff)

def choix(self,coiffure_slug,**kwargs):
    
    data = coiffuresGaleries.objects.get(nom_coi=coiffure_slug)
    print(data)
    t = coiffuresGaleries.objects.all()
    context={'d':data,'g':t}

  
    return render(self,'choix.html',context,**kwargs)

def search(request):
   
        search = request.GET['search']
        counts = coiffuresGaleries.objects.filter(nom_coi__icontains=search).count()
        afftouteListe=coiffuresGaleries.objects.all().filter(nom_coi__icontains=search)
        if not afftouteListe:
            messages.error(request,f"{counts} résultat pour '{search}' ")
            return render(request,'search.html',{'afftouteListe':afftouteListe})
            
        else:
            if counts > 1:
                messages.success(request,'{} Résultats de recherche pour {}'.format(counts,search))
                return render(request,'search.html',{'afftouteListe':afftouteListe})
            elif counts == 1:
                messages.success(request,'{} Résultat de recherche pour {}'.format(counts,search))
                return render(request,'search.html',{'afftouteListe':afftouteListe})
                 

def contact(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        email = request.POST['email']
        message = request.POST['message']

        if Contacts.objects.filter(email_con=email):
            messages.error(request,'Cet email existe déjà !')
            return render(request,'contact.html')
        elif email == '' or email is None:
            messages.error(request,"Champ est obligatoire !")
            return redirect('contact')
        elif message == '' or message is None:
            messages.error(request,'Champ est obligatoire !')
            redirect('contact')
        elif nom is None:
            messages.error(request,'Champ est obligatoire !')
            redirect('contact')
        elif request.method is None:
            messages.error(request,'Champ est obligatoire !')
            redirect('contact')
        else:
            createContact = Contacts.objects.create(nom_con=nom,email_con=email,message_con=message)
            createContact.save()
            messages.success(request,'Message envoyé avec succès')
            return render(request,'contact.html')
    # else:
    #     messages.error(request,"Veuillez remplir les champs !")
    #     return render(request,'contact.html')
    return render(request,'contact.html')
    


def contacts(req):
    if req.method == 'POST':
        nom = req.POST['nom']
        email = req.POST['email']
        message = req.POST['message']

        if Contacts.objects.filter(email_con=email):
            messages.error(req,'Cet email existe déjà !')
            return render(req,'contact.html')
        elif email == '' or email is None:
            messages.error(req,"Champ est obligatoire !")
            return redirect('contact')
        elif message == '' or message is None:
            messages.error(req,'Champ est obligatoire !')
            redirect('contact')
        elif nom is None:
            messages.error(req,'Champ est obligatoire !')
            redirect('contact')
        elif req.method is None:
            messages.error(req,'Champ est obligatoire !')
            redirect('contact')
        else:
            createContact = Contacts.objects.create(nom_con=nom,email_con=email,message_con=message)
            createContact.save()
            messages.success(req,'Message envoyé avec succès')
            return render(req,'contact.html')
    # else:
    #     messages.error(request,"Veuillez remplir les champs !")
    #     return render(request,'contact.html')
    return render(req,'contact.html')
    

     
       
 
