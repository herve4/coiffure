from django import forms
from coiffuresapp.models import coiffuresGaleries,client
from django.contrib.auth.models import User



# class formsValidate(forms.ModelForm):
#     nom_auth = forms.CharField(queryset= User.objects.get() ,label="Nom",widget=forms.TextInput(attrs={'Class':'form-control'}))
#     #email_auth = forms.EmailField(label="Email",widget=forms.EmailInput(attrs={'Class':'form-control'}))
#     # email = forms.CharField(label="Email",widget=forms.PasswordInput(attrs={'Class':'form-control'}))

#     class Meta:
#         model = coiffuresGaleries
#         fields = ['days_coi','time_coi','nom_auth']
#         label = {'days_coi':'Date pour vous coiffer','time_coi':'Quelle heure ?'}
# class formsValidate(forms.ModelForm):

#     class Meta:
#         model = coiffuresGaleries
#         fields = ['days_coi','time_coi']
#         label = {'days_coi':'Date pour vous coiffer','time_coi':'Quelle heure ?'}
# class formUser(AbstractUser):
#     class Meta:
#         fields = ['username','email']

        #  nom_ar = forms.TextInput(attrs={'class':'form-control'})
        #     desc_ar = forms.Textarea(attrs={'class':'form-control'})
           
        #     categories_ar = forms.Select(attrs={'class':'form-control'})
           
           

        #     widgets= {
        #                 'nom_ar':nom_ar,
        #                 'desc_ar':desc_ar,
        #                 'categories_ar':categories_ar,
                        
        #     }
               