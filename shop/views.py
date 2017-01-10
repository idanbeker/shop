from django.shortcuts import render
from .models import User, Item
import logging


def index(request):
    user = User.objects.get(id='1')

    # Next page case - change item filter
    if request.POST.get('gotopage'):
        user.page_index = int(request.POST.get('topage')) - 1
        user.save()
    items = selectItems(user)

    context = {'user': user,
               'items': items,
               'num_pages': int((Item.objects.all().__len__()) / 6)
               if (Item.objects.all().__len__() % 6 == 0 )
               else int((Item.objects.all().__len__()) / 6) + 1
               }
    # Add item to cart case
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
        cart_item = {'item': item,
                     'quantity': quantity,
                     'total': total_item
                     }
        cart.append(cart_item)
    context = {'user': user, 'cart': cart, 'items': items, 'total': total_cart}
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


def selectItems(user):
    items = Item.objects.all()
    current_page = user.page_index

    return items.filter(id__gt=current_page * 6).filter(id__lt=1 + (current_page + 1) * 6)
