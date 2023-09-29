from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def auth_coiffeur(request):
    return render(request,'login.html')


class loginAuthview(TemplateView):
    template_name = 'login.html'
    def post(self, request, **kwargs):
        if request.method == 'POST':
            username = request.POST['username']            
            pwd = request.POST['pwd']
            user = authenticate(username=username,password=pwd)
            if user is not None and user.is_active:
                login(request, user)
                messages.success(request,"Compte crée avec succès")
                return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL,**kwargs)
            else:
                messages.error(request,"Nom d'utilisateur ou mot de passe incorrect !")
                redirect(self.template_name)
        return render(request, self.template_name)
            

class logoutView(TemplateView):
    template_name = 'login.html'
    def get(self, request, **kwargs):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)
    


def creation(request):
   
        
        if request.method == 'POST' :
            username = request.POST['username']
            email = request.POST['email']
            pwd = request.POST['pwd']
            pwd2 = request.POST['pwd2']
        
            if User.objects.filter(username=username):
                messages.error(request,"Ce nom existe déjà !")
                return render(request,'inscription.html')
            elif User.objects.filter(email=email):
                messages.error(request,"Cet email existe déjà !")
                return render(request,'inscription.html')
            elif pwd != pwd2:
                messages.error(request,"Le mot de passe ne corespond pas!")
                return render(request,'inscription.html')
            else:
                user = User.objects.create_user(username=username,email=email,password=pwd)
                user.save()
                messages.success(request,"Compte crée avec succès !")
                return HttpResponseRedirect(settings.LOGIN_URL)
        
        
        return render(request,'inscription.html')




