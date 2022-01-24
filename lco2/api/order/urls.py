
from .views import OrderViewSet ,add
from django.urls import path ,include


from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', OrderViewSet)
urlpatterns =[
    path("",include(router.urls)),
    path("add/<str:id>/<str:token>/" ,add)
]