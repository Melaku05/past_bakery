from django.db import models
from users.models import CustomUser
import time
import random
import string
from django.utils.text import slugify
from django.utils.html import strip_tags
import html
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO
from django.utils.text import slugify
import uuid


class Bankname(models.Model):
    name = models.CharField(max_length=200)
    account = models.CharField(max_length=250)
    slug = models.SlugField(max_length=200, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        super().save(*args, **kwargs)
    
class Paywithbank(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=11, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    out_trade_no = models.CharField(max_length=60, editable=False)
    transaction_no = models.CharField(max_length=100, blank=False)
    payment_status = models.BooleanField(default=False)
    screenshot = models.ImageField(upload_to='images/bank', blank=False)
    bank_name = models.CharField(max_length=200)
    ref_number = models.CharField(max_length=200, unique=True)
    user_bank_account_name = models.CharField(max_length=200)
    paid_by_bank = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=13, blank=False)


    def save(self, *args, **kwargs):
        if not self.transaction_no:
            self.transaction_no = str(int(time.time() * 1000)) + ''.join(random.choices(string.ascii_letters + string.digits, k=3))

        try:
                # Check if the object already exists in the database
            this = Paywithbank.objects.get(id=self.id)
            if this.screenshot != self.screenshot:
                this.screenshot.delete(save=False)
        except Paywithbank.DoesNotExist:
            pass  # When it's a new object, do nothing
        
                # Optimize image before saving
        if self.screenshot:
            img = Image.open(self.screenshot)
            output = BytesIO()

            # Save the image in its original format
            img_format = img.format
            img.save(output, format=img_format, quality=75)
            output.seek(0)

            # Define a proper upload path for the image
            upload_path = 'images/bank/{}.{}'.format(uuid.uuid4(), img_format.lower())
            self.screenshot = ContentFile(output.read(), upload_path)

        super().save(*args, **kwargs)


    def delete(self, *args, **kwargs):
        self.screenshot.delete(save=False)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.transaction_no
    