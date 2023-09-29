from django.db import models
from auth_coiffeur.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save
from phonenumber_field.modelfields import PhoneNumberField
from django_resized import ResizedImageField
from random import random,randint

class slider(models.Model):
    image = ResizedImageField(size=[1920, 1080], crop=['middle', 'center'], upload_to='media/slider')
    titre = models.CharField(max_length=255,verbose_name="Titre",null=True)
    paragraphe = models.CharField(max_length=60, verbose_name="Paragraphe", null=True)

    def __str__(self) -> str:
        return self.titre
    class Meta:
        verbose_name='Slider'
        verbose_name_plural = 'Sliders'

class typeCoiffure(models.Model):
    name=models.CharField(max_length=25, verbose_name="Coiffure pour",unique=True)
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name='Coiffure pour'
        verbose_name_plural = 'Coiffures pour'
        

class categorisCoiffures(models.Model):
    coiffurePour = models.ForeignKey(typeCoiffure,on_delete=models.CASCADE,verbose_name='Coiffure pour',null=True)
    img_couverture = ResizedImageField(size=[350, 350], crop=['middle', 'center'], upload_to='media/catégories',null=True)
    nom_cat = models.CharField(unique=True,verbose_name='Catégorie',max_length=60)

    def __str__(self) -> str:
        return self.nom_cat
    class Meta:
        verbose_name='Catégorie'
        verbose_name_plural = 'Catégories'

class paie(models.Model):
    type = models.CharField(max_length=15,null=True,blank=True,verbose_name='Type')

    
    def __str__(self) -> str:
        return self.type
    class Meta:
        verbose_name='Paie'
        verbose_name_plural = 'Paies'




class coiffuresGaleries(models.Model):
    coiffurePour = models.ForeignKey(typeCoiffure,on_delete=models.CASCADE,verbose_name='Coiffure pour',null=True)
    categorieCoiffures = models.ForeignKey(categorisCoiffures,on_delete=models.CASCADE,verbose_name='Catégorie',null=True)
    nom_coi = models.CharField(unique=True, verbose_name='Coiffure',max_length=60)
    desc_coi = models.TextField(max_length=255,verbose_name='Description')
    prix_coi = models.CharField(verbose_name='Prix',max_length=12)
    img_coi = ResizedImageField(size=[350, 350], crop=['middle', 'center'], upload_to='media')
    slugs = models.SlugField(default="",max_length=500,null=True,blank=True)
    created_coi= models.DateTimeField(auto_now_add=True,verbose_name='Date de publication')
    update_coi = models.DateTimeField(auto_now=True,verbose_name='Date de modification')
   
    
    def __str__(self) -> str:
        return self.nom_coi
    class Meta:
        verbose_name='Coiffure'
        verbose_name_plural = 'Coiffures'
        
    def get_absolute_url(self):
        return reverse("show", kwargs={"slugs": self.slugs})
    
    def getAllCoiffures(self):
        coiffure = coiffuresGaleries.objects.filter(slugs=self.slugs)
        return coiffure

def create_slug(instance, new_slug=None):
    slugs = slugify(instance.nom_coi)

    if new_slug is not None:
        slugs = new_slug
    q = coiffuresGaleries.objects.filter(slugs=slugs).order_by('-id')
    exister = q.exists()
    if exister:
        new_slug = "%s-%s"%(slugs,q.first().id)
        return create_slug(instance,new_slug=new_slug)
    return slugs

def pre_save_post_receiver(sender,instance, *args, **kwargs):
    if not instance.slugs:
        instance.slugs = create_slug(instance)
pre_save.connect(pre_save_post_receiver,coiffuresGaleries)



class client(models.Model):
    paie = models.CharField( verbose_name='Paiement',max_length=60,null=True)
    nom_cl = models.CharField(max_length=25, verbose_name='Nom')
    email_cl = models.EmailField(max_length=50,verbose_name='Email',unique=True,blank=True)
    secret = models.CharField(max_length=1000,default="",blank=True,verbose_name='ID client')
    montant = models.CharField(max_length=6,default=0, verbose_name="Montant")
    telephone_cl = models.CharField(max_length=12,blank=True,unique=True, error_messages='Ce numéro existe déjà !', verbose_name="Téléphone")
    adresse_cl = models.CharField(max_length=60,verbose_name='Adresse', null=True, blank=True)
    time_coi = models.TimeField(verbose_name='Heure',null=True)
    days_coi = models.DateField(verbose_name='Jour pour la coiffure',null=True)
    coiffure = models.ForeignKey(coiffuresGaleries, on_delete=models.CASCADE,verbose_name='Coiffure', null=True )
    payer = models.BooleanField(null=True, blank=True)

    def generate_secret(self):
        self.secret = random.randrange(10000,99999)
        
        
    def __str__(self) -> str:
        return self.nom_cl
    class Meta:
        verbose_name='Client'
        verbose_name_plural = 'Clients'





class commentaireCoiffure(models.Model):
    com_coi = models.TextField(verbose_name='Commentaire',null=True,max_length=255)
    coiffure_id_com = models.ForeignKey(coiffuresGaleries, on_delete=models.CASCADE,verbose_name='Coiffures')

    def __str__(self) -> str:
        return self.com_coi
    class Meta:
        verbose_name='Commentaire'
        verbose_name_plural = 'Commentaires'

class Contacts(models.Model):
    nom_con = models.CharField(max_length=35,verbose_name='Nom contact')
    email_con = models.EmailField(max_length=255,verbose_name='Email',unique=True)
    message_con = models.TextField(verbose_name='Message',max_length=255)

    def __str__(self) -> str:
        return self.nom_con
    class Meta:
        verbose_name='Contact'
        verbose_name_plural = 'Contacts'




