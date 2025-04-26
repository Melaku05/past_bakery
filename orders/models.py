from django.db import models
import random
import string
from users.models import CustomUser
from store.models import Product


def generate_unique_order_key():
    """Generate a unique 6-character order key."""
    for _ in range(10):  # Try 10 times max
        letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
        numbers = ''.join(random.choice(string.digits) for _ in range(3))
        order_key = letters + numbers
        if not Order.objects.filter(order_key=order_key).exists():
            return order_key
    raise Exception("Could not generate a unique order key after 10 tries")


class Order(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    order_phone = models.CharField(max_length=13, blank=True)
    order_username = models.CharField(max_length=50, blank=True, null=True)
    order_address = models.CharField(max_length=100)
    order_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    order_key = models.CharField(max_length=6, editable=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.order_key:
            self.order_key = generate_unique_order_key()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.order_key)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    product_owner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    delivered = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.product and self.product.product_owner:
            self.product_owner = self.product.product_owner
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product_name} ({self.quantity})'
