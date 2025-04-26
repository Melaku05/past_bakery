from django.urls import path
from carts import views
# from telebirrpay.views import MakePaymentView

urlpatterns = [
    path('', views.cart, name="cart"),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('increase_cart_item/<int:product_id>/<int:cart_item_id>/', views.increase_cart_item, name='increase_cart_item'),
    path('remove_cart/<int:product_id>/<int:cart_item_id>/', views.remove_cart, name='remove_cart'),
    path('remove_cart_item/<int:product_id>/<int:cart_item_id>', views.remove_cart_item, name='remove_cart_item'),
    # path('clear_cart/', views.clear_cart, name='clear_cart'),
    #path('make_payment/', MakePaymentView.as_view(), name='make_payment'),
]
