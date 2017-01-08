from django.shortcuts import render
from .models import User, Item
import logging



def index(request):
    user = User.objects.get(id='1')
    items = Item.objects.all()
    context = {'user': user, 'items': items}
    if request.POST.get('additem'):
        addToCart(request, context)

    return render(request, 'shop/shop.html', context)


def cart(request):
    user = User.objects.get(id='1')
    items = Item.objects.all()
    cart_list = user.cart.split()
    cart_list_uniq = set(cart_list)
    cart = []
    total_cart = 0
    # can do with map
    for x in cart_list_uniq:
        item = Item.objects.get(pk=x)
        quantity = cart_list.count(x)
        total_item = quantity * item.price
        total_cart += total_item
        cart_item = {'item' : item ,
                'quantity' : quantity ,
                'total' : total_item
                }
        cart.append(cart_item)
    print(type(cart))
    context = {'user': user, 'cart' : cart ,'items' :items , 'total': total_cart}
    return render(request, 'shop/cart.html', context)


def addToCart(request, context):
    user = context['user']
    user.cart_size += int(request.POST.get('quantity'))
    logger = logging.getLogger(__name__)
    logger.error('user cart =' + user.cart)
    if user.cart == 'EMPTY':
        user.cart = (request.POST.get('productid') + ' ') * int(request.POST.get('quantity'))
    else:
        user.cart += (' ' + request.POST.get('productid')) * int(request.POST.get('quantity'))
    user.save()
