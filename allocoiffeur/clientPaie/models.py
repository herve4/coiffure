from random import random
from django.db import models



# class Paiement(models.Model):
#     client = models.ForeignKey(client,on_delete=models.CASCADE,null=True)
#     coiffure = models.ForeignKey(coiffuresGaleries,on_delete=models.CASCADE)
#     secret = models.CharField(max_length=1000,default="",blank=True,verbose_name='ID client')
#     montant = models.DecimalField(default=0,decimal_places=3,max_digits=3)
#     payer = models.BooleanField(default=False, verbose_name='Payé')
#     checkout_url = models.CharField(max_length=1000,default="",blank=True)
#     # datePaie = models.DateTimeField(auto_now_add=True,verbose_name='Date paiement')

#     def generate_secret(self):
#         self.secret = str(random.randint(10000,99999))

#     def __str__(self) -> str:
#         return self.secret
#     class Meta:
#         verbose_name = "Paiement"
#         verbose_name_plural = "paiements"
