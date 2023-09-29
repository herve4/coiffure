from django import forms
from coiffuresapp.models import client
from auth_coiffeur.models import User

class clientForm(forms.Form):
   
    class Meta:
        model = client
        fields = ['__all__']
        

        