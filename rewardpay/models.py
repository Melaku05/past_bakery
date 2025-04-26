from django.db import models
from users.models import CustomUser
import time
import random
import string

# Create your models here.


class RewardRate(models.Model):
    user_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.01)
    referral_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.01)
    user_referral_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.01)

class PaywithReward(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=11, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    out_trade_no = models.CharField(max_length=60, editable=False)
    transaction_no = models.CharField(max_length=100, blank=True)
    payment_status = models.BooleanField(default=True)
 
 
    def save(self, *args, **kwargs):
        if not self.transaction_no:
            self.transaction_no = str(int(time.time() * 1000)) + ''.join(random.choices(string.ascii_letters + string.digits, k=3))
        super().save(*args, **kwargs)


    def __str__(self):
        return self.transaction_no
    