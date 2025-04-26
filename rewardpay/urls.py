from django.urls import path
from .views import pay_with_reward

from . import views

urlpatterns = [
    path('pay_with_reward/', pay_with_reward, name='pay_with_reward'),
    
]