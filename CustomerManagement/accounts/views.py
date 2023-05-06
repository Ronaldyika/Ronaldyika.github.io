from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.



def customer(request):
    det = Customer.objects.all()
    all = Order.objects.all()
    order_count = all.count()
    context = {
        'det':det,
        'all':all,
        'order_count': order_count
    }
    return render(request,'accounts/customer.html',context)

def products(request):

    return render(request,'accounts/products.html')
def dashbord(request):
    detail = Order.objects.all()
    order_count = detail.count()
        
    context = {
        'details': detail,
        'order_count': order_count
    }
    

    return render(request,'accounts/dashbord.html',context)