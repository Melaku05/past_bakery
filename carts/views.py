from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from store.models import Product
from uuid import uuid4
from decimal import Decimal
from django.http import Http404
from django.http import JsonResponse

def _cart_id(request):
    cart_id = request.session.get('cart_id')
    if cart_id is None:
        cart_id = str(uuid4())
        request.session['cart_id'] = cart_id
    else:
        cart_id = str(cart_id)  
    return cart_id



def add_cart(request, product_id):
    if request.method == 'POST':
        try:
            product = get_object_or_404(Product, id=product_id)
            cart_id = _cart_id(request)
            cart, _ = Cart.objects.get_or_create(cart_id=cart_id)
        

            cart_item, created = CartItem.objects.update_or_create(
                product=product,
                cart=cart,
                product_name=product.product_name,
                defaults={
                    'quantity': 1, 
                    'category': product.category.category_name,
                }
            )

            if not created:
                cart_item.quantity += 1

            cart_item.product_image_url = product.get_main_image().image.url if product.get_main_image() else ''
            cart_item.save()

            return redirect('cart')

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid method"}, status=400)


def remove_cart(request, product_id, cart_item_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except:
        pass
    return redirect('cart')

def increase_cart_item(request, product_id, cart_item_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_item = get_object_or_404(CartItem, product__id=product_id, cart=cart, id=cart_item_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

def remove_cart_item(request, product_id, cart_item_id):
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            product = get_object_or_404(Product, id=product_id)
            cart_item = get_object_or_404(CartItem, product=product, cart=cart, id=cart_item_id)
            cart_item.delete()
        except Http404:
           return redirect('cart')
        return redirect('cart')


def cart(request, total=0, quantity=0, cart_items=None):
   
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.select_related('product').filter(cart=cart, is_active=True).order_by('id')
        for cart_item in cart_items:
            quantity += cart_item.quantity

    except ObjectDoesNotExist:
        pass

    context = {
        'cart_items': cart_items,
        'quantity': quantity,
    }
    return render(request, 'cart.html', context)


def clear_cart(request):
    cart_id = _cart_id(request)
    try:
        cart = Cart.objects.get(cart_id=cart_id)
        cart.items.all().delete()
        del request.session['cart_id']
    except Cart.DoesNotExist:
        pass
    return redirect('orders')
 