from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views import generic
from .models import User, Item


def index(request):
    user = User.objects.get(id='1')
    items = Item.objects.all()
    context = {'user': user, 'items': items}
    if request.POST.get('mybtn'):
        user.cart_size += int(request.POST.get('quantity'))
        user.save()
    return render(request, 'shop/shop.html', context)


def cart(request):
    user = User.objects.get(id='1')
    context = {'user': user}
    return render(request, 'shop/cart.html', context)





