from django.shortcuts import render
from django.http import JsonResponse
from users.models import CustomUser
from orders.models import Order
from .models import PaywithReward
from django.urls import reverse
from decimal import Decimal


# Create your views here.


def pay_with_reward(request):
    if request.method == 'POST':
        user = CustomUser.objects.get(email=request.user.email)
        order = Order.objects.filter(user=request.user, payment_status=False).latest('order_date')
        total_amount = Decimal(order.order_total_prices)

        if user.point_reward >= total_amount:
            user.point_reward -= total_amount
            user.save()

            payment = PaywithReward(
                user=user,
                total_amount=total_amount,
                out_trade_no=order.outTradeNo,
            )
            payment.save()

            order.payment_status = True
            order.paid_by_points = True
            order.transaction_no = payment.transaction_no
            if user.phone_number:
                order.order_phone = user.phone_number
            order.save()

            return JsonResponse({'success': True, 'redirect_url':  reverse('order_complete')})  # Update with your success URL
        else:
            return JsonResponse({'success': False, 'message': 'Insufficient reward points.'})

    return JsonResponse({'success': False, 'message': 'Invalid request.'})