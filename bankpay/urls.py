from django.urls import path
from .views import pay_with_bank,index

from . import views

urlpatterns = [
    path('pay_with_bank/', pay_with_bank, name='pay_with_bank'),
    path('bankpay/', index, name="bankpay"),
    
]