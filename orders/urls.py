# orders/urls.py
from django.urls import path
from . import views
from .views import export_orders_pdf, export_orders_xlsx
# app_name = 'orders'
urlpatterns = [
    path('', views.checkout, name='orders'),
    path('create_order/', views.create_order, name='create_order'),
    path('order_complete/', views.order_complete, name='order_complete'),
    path('export/', views.export_view, name='export'),
    path('orders/export_orders/pdf/', export_orders_pdf, name='export_orders_pdf'),
    path('orders/export_orders/xlsx/', export_orders_xlsx, name='export_orders_xlsx'),
    path('export_orders/', views.export_orders_view, name='export_orders'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
]