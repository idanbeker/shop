from django.shortcuts import render
from .models import User , Item


def index(request):
    user = User.objects.get(id='1')
    context = {'user' : user }
    return render(request,'shop/shop.html',context)

def cart(request):
    user = User.objects.get(id='1')
    context = {'user' : 'test'}
    return render(request, 'shop/cart.html',context)

