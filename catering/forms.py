from django import forms
from .models import Catering

class CateringForm(forms.ModelForm):
    class Meta:
        model = Catering
        fields = ['number_of_person', 'date', 'catering_type', 'location', 'full_name', 'email', 'phone']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
