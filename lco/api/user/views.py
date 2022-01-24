from rest_framework import permissions
from .serializers import UserSerializer
from django.shortcuts import render
from rest_framework import status ,viewsets
from rest_framework.permissions import AllowAny
from .models import CustomUser
from django.http import JsonResponse
from django.contrib.auth import get_user_model ,login,logout
from django.views.decorators.csrf import csrf_exempt
import re


# Create your views here.
import random

def generate_session_token(length=10):
    return "".join(random.SystemRandom().choice([chr(i) for i in range(97,123)+[str(i) for i in range(10)]])for _ in range(length))

@csrf_exempt
def signIn(request):
    if not request.method=='POST':
        return JsonResponse({"error":"send a post request only"})
    username=request.POST["email"]
    password=request.POST["password"]

    if not re.match("([\w\.\-_]+)?\w+@[\w-_]+(\.\w+){1,}" ,username):
        return JsonResponse({"error":"send a valid email"})
    if(len(password)<3):
        return JsonResponse({"error":"password should be at least three characters"})

    userModel=get_user_model()


    try :
        user=userModel.objects.get(email=username)
        if user.check_password(password):
            user_dict=userModel.objects.filter(email=username).values().first()
            user_dict.pop("password")

            if user.session_token !="0":
                user.session_token ="0"
                user.save()
                return JsonResponse({"error":"Previous session exitsts"})
            token=generate_session_token()
            user.session_token=token
            user.save()
            login(request,user)
            return JsonResponse({"token" : token, "user" :user_dict})  
        else:
            return JsonResponse({"error":"Invalid password "})

    except userModel.DoesNotExist:
        return JsonResponse({"error":"Invalid Email"})


def signOut(request ,id):
    logout(request)
    userModel=get_user_model()
    try :
        user=userModel.objects.get(pk=id)
        user.session_token ="0"
        user.save()
    except userModel.DoesNotExist:
        return JsonResponse({"error":"Invalid User Id "})




class UserViewSet(viewsets,viewsets.ModelViewSet):
    permission_classes_by_action={'create':[AllowAny]}
    queryset=CustomUser.objects.all().order_by("id")
    serializer_class = UserSerializer

    def get_permissions(self):
        try :
            return [ permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [ permission() for permission in self.permission_classes]



