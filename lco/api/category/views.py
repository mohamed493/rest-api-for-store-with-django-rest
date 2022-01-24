from django.db.models.query import QuerySet
from rest_framework import viewsets

from .serializers import CategorySerializer
from .models import Category



class CategoryViewSet(viewsets.ModelViewSet):
     queryset = Category.objects.all()
     print("////////////////",queryset)
     serializer_class = CategorySerializer


