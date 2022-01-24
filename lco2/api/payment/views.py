from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

import braintree

# Create your views here.
def validate_user_session(id ,token):
    userModel=get_user_model()
    try:
        user=userModel.objects.get(pk=id)
        if user.session_token ==token:
            return True 
        return False
    except userModel.DoesNoeExist:
        return False


gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id="cppsvvkbwqvwzhrs",
        public_key="h4xc7jfvb4dmxdbd",
        private_key="4e0575adf0758428d127252a6fe89675"
    )
)

@csrf_exempt
def generate_token(request , id,token):
    if not validate_user_session(id,token):
        return JsonResponse({"error":"Invalid session ,please login again"})
    client_token = gateway.client_token.generate({
    "customer_id": id})
    return client_token



@csrf_exempt
def process_payement(request , id,token):
    if not validate_user_session(id,token):
        return JsonResponse({"error":"Invalid session ,please login again"})

    nonce_from_the_client=request.POST["payment_method_nonce"]
    amount_from_the_client=request.POST["amount"]


    result = gateway.transaction.sale({
    "amount": "amount_from_the_client",
    "payment_method_nonce": nonce_from_the_client,
    "options": {
      "submit_for_settlement": True
    }})
    if result.is_success:
        return JsonResponse({"sucess":result.is_success})
    else:
      return JsonResponse({"success":False}) 



