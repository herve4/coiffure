from django.shortcuts import render
from .models import *

def coiffuresapp(request):
    hommes = coiffuresGaleries.objects.filter(coiffurePour__name='Hommes')
    femmes = coiffuresGaleries.objects.filter(coiffurePour__name='Femmes')
    sliders = slider.objects.all()
    context = {'hommes':hommes,'femmes':femmes,'sliders':sliders}
    return render(request,'index.html',context)

def page404(request):
    return render(request,'404.html')


