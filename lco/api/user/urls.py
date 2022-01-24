
from django.contrib.auth.models import User
from .views import ProductViewSet ,signIn ,signOut
from django.urls import path ,include
from .views import UserViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', UserViewSet)
urlpatterns =[
    path("login/",signIn,name="signIn"),
    path("logout/<int:id>/",signOut,name="signOut"),
    path("",include(router.urls))
]