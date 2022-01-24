
from django.db.models import fields
from rest_framework import serializers

from .models import Product


class ProductSerializers(serializers.ModelSerializer):
    image=serializers.ImageField(max_length=None, allow_empty_file=False,allow_null=True,required=False)

    class Meta:
        model=Product
        fields=("id" ,"name" ,"description" ,"category" ,"price" ,"image")

    
