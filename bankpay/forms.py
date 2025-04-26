from django import forms

class BankpayForm(forms.Form):
    bank_name = forms.CharField(max_length=20, required=True)
    phone_number = forms.CharField(max_length=13, required=True)
    ref_number = forms.CharField(max_length=20, required=True)
    user_bank_account_name = forms.CharField(max_length=30, required=True)
    screenshot = forms.ImageField(required=False)