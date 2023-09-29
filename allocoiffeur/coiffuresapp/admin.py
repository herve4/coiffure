from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import *



admin.site.register(slider)
admin.site.register(paie)
admin.site.register(typeCoiffure)
admin.site.register(commentaireCoiffure)
admin.site.register(categorisCoiffures)



class clientInline(admin.StackedInline):
        model = client
class InlineUser(UserAdmin):
    inlines = (clientInline,)
@admin.register(client)
class clientList(admin.ModelAdmin):

    
    list_display = ['secret','nom_cl','email_cl','telephone_cl','paie','time_coi','days_coi']
    list_filter = ['nom_cl','email_cl']
    list_display_links = ['nom_cl','email_cl']
    search_fields = ['nom_cl']

    fieldsets = [
        ('Informations client',{'fields':[('secret','nom_cl','email_cl'),'telephone_cl','adresse_cl']}),
        ('Réservation',{'fields':['coiffure','time_coi','days_coi']}),
        ('Paiements',{'fields':['paie']}),
    ]

@admin.register(coiffuresGaleries)
class coiffureList(admin.ModelAdmin):

    
    list_display = ['__str__','prix_coi','img_coi','created_coi','update_coi']
    search_fields = ['nom_coi']

    # fieldsets = [
    #     ('Réservation coiffeur',{'fields':[('categorieCoiffures','nom_coi','desc_coi'),'prix_coi','img_coi','slugs']}),
    # ]


@admin.register(Contacts)
class coiffureList(admin.ModelAdmin):

    
    list_display = ['__str__','nom_con','email_con','message_con']
    search_fields = ['nom_con']

    fieldsets = [
        ('Nouveau message',{'fields':[('nom_con','email_con'),'message_con']}),
    ]

