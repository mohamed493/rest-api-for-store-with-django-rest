

# Create your views here.
from django.db.models.query import QuerySet
from rest_framework import viewsets

from .serializers import ProductSerializers
from .models import Product



class ProductViewSet(viewsets.ModelViewSet):
     queryset = Product.objects.all().order_by("id")
     one_entry = Product.objects.get(id=1)
     print(one_entry.name)
     for product in queryset:
          if(product.name=='ff'):
               product.name='nice_shirt'
               product.save()   
     serializer_class = ProductSerializers


