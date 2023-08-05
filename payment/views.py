from django.shortcuts import render
from .models import ShippingAddress
# Create your views here.

def payment_success(request):

    return render(request, 'payment/payment-success.html')

def payment_failed(request):

    return render(request, 'payment/payment-failed.html')

def checkout(request):

    #Users with accounts --Prefill the form

    if request.user.is_authenticated:

        try:
            #Authenticated users with shipping information

            shipping_address = ShippingAddress.objects.get(user = request.user.id)
            
            context = {
                'shipping': shipping_address,
            }

            return render(request, 'payment/checkout.html', context)

        except:

            #Authenticated users with no shipping information

            return render(request, 'payment/checkout.html')
    
    else:
        #Guest users

        return render(request, 'payment/checkout.html')
