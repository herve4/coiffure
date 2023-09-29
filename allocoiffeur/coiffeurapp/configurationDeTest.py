from django.core.paginator import Paginator

Malist = ['Réné','Henri','Fulbert','Sami']
p = Paginator(Malist, 2)
p.page_range