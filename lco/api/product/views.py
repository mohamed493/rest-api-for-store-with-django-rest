

# Create your views here.
from django.db.models.query import QuerySet
from rest_framework import viewsets

from .serializers import ProductSerializers
from .models import Product



class ProductViewSet(viewsets.ModelViewSet):
     queryset = Product.objects.all().order_by("id")
     print("YYYYYYYYYyyyyYYYYYYyyYYYyyYYYYy",queryset)
     serializer_class = ProductSerializers


