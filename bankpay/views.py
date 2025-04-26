from django.shortcuts import render
from django.http import JsonResponse
from users.models import CustomUser
from orders.models import Order
from .models import Paywithbank, Bankname
from django.urls import reverse
from decimal import Decimal
from .forms import BankpayForm
from users.models import CustomUser
from rewardpay.models import RewardRate

# Create your views here.
def index(request):
    banks = Bankname.objects.all()  # Retrieve all Bankname objects
    return render(request, 'bankpay.html', {'banks': banks})



def pay_with_bank(request):
    if request.method == 'POST':
        print("POST request received")
        user = CustomUser.objects.get(username=request.user.username)
        order = Order.objects.filter(user=request.user, payment_status=False).latest('order_date')
        total_amount = Decimal(order.order_total_prices)

        form = BankpayForm(request.POST, request.FILES)
        if form.is_valid():
            print("Bank Account Name:", form.cleaned_data['user_bank_account_name'])
            print("Screenshot:", form.cleaned_data['screenshot'])
            print("phone number", form.cleaned_data['phone_number'])
            print("ref number", form.cleaned_data['ref_number'])
            payment = Paywithbank(
                bank_name=form.cleaned_data['bank_name'],
                phone_number=form.cleaned_data['phone_number'],
                ref_number=form.cleaned_data['ref_number'],
                user_bank_account_name=form.cleaned_data['user_bank_account_name'],
                screenshot=form.cleaned_data['screenshot'],
                user=user,
                total_amount=total_amount,
                out_trade_no=order.outTradeNo,
            )
            payment.save()
            order.transaction_no = payment.transaction_no
            order.order_phone = payment.phone_number
            order.bank_ref_number = payment.ref_number
            order.save()
            user.phone_number = payment.phone_number
            user.save()

            return JsonResponse({'success': True, 'redirect_url':  reverse('order_complete')})  # Update with your success URL
        else:
            return JsonResponse({'success': False, 'message': 'Please fill in all the required information in the form.'})

    return JsonResponse({'success': False, 'message': 'Invalid request.'})