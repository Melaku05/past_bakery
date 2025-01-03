from django.db import models


class Catering(models.Model):
    CATERING_CHOICES = [
        ('wedding', 'Breakfast'),
        ('birthday', 'Birthday Catering'),
        ('holiday', 'Holiday Catering'),
        ('corporate', 'Corporate Catering'),
        ('private', 'Private Party Catering'),
        ('event', 'Event Catering'),
        ('buffet', 'Buffet Catering'),
    ]
    catering_type = models.CharField(max_length=10, choices=CATERING_CHOICES)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    number_of_person = models.IntegerField()
    date = models.DateField()
    email = models.EmailField(blank=True, null=True)
    location = models.CharField(max_length=255)
  
    def __str__(self):
        return f"{self.full_name} - {self.date}"