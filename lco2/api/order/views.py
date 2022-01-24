from .models import Order
#from api.product.models import Product
from rest_framework import viewsets
from django.http import JsonResponse
from django.contrib.auth import get_user_model

from .serializers import OrderSerializer


from django.views.decorators.csrf import csrf_exempt


def validate_user_session(id ,token):
    userModel=get_user_model()
    try:
        user=userModel.objects.get(pk=id)
        if user.session_token ==token:
            return True 
        return False
    except userModel.DoesNoeExist:
        return False



@csrf_exempt
def add(request ,id ,token):
    if not validate_user_session(id,token):
        return JsonResponse({"error":"please login"})
    if request.method=="POST":
        print(request.POST)
        user_id=id
        transaction_id=request.POST["transactions_id"]
        amount=request.POST["total_amount"]
        products=request.POST["product_names"]
      #  total_pro=len(products.split(","[:-1]))
        userModel=get_user_model()

        try:
            user=userModel.objects.get(pk=user_id)
            ordr=Order(user=user ,product_names=products ,total_amount=amount,transactions_id=transaction_id)
            ordr.save()
            return JsonResponse({"success":True ,"msg":'this ordered sucessfully'})

        except userModel.DoesNoeExist:
            return JsonResponse({"error":"user does not exist"})




class OrderViewSet(viewsets.ModelViewSet):
     queryset = Order.objects.all()
     print("////////////////",queryset)
     serializer_class = OrderSerializer



