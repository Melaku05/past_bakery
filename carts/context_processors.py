from . models import Cart,  CartItem
from .views import _cart_id

def counter(request):
    cart_id = _cart_id(request)
    cart, _ = Cart.objects.get_or_create(cart_id=cart_id)
    cart_items = CartItem.objects.filter(cart=cart)
    count = 0
    if cart_items:
        for cart_item in cart_items:
            count += cart_item.quantity
    return dict(cart_item_count=count)