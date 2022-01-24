
from .views import generate_token ,process_payement
from django.urls import path ,include


urlpatterns =[
    path("process/<str:id>/<str:token>/" ,process_payement),
    path("gettoken/<str:id>/<str:token>/" ,generate_token),
]