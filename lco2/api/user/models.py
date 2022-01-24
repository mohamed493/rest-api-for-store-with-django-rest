from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser 



class CustomUser(AbstractUser):
    name=models.CharField(max_length=255,default='Anonoyms')
    email=models.EmailField(max_length=255 ,unique=True)
    username=None
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["name"]
    phone=models.CharField(max_length=255,blank=True ,null=True)
    gender=models.CharField(max_length=255,blank=True ,null=True)
    session_token=models.CharField(max_length=10 ,default=0)

    created_at=models.DateTimeField(auto_now_add=True)
    updates_at=models.DateTimeField(auto_now=True)
