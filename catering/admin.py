from django.contrib import admin
from .models import Catering
from msigana_ecommerce.admin_site import admin_site


class CateringAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'date', 'number_of_person', 'location', 'catering_type', 'email', 'phone')
    list_filter = ('date','catering_type')
    search_fields = ('full_name', 'email', 'phone')
admin_site.register(Catering, CateringAdmin)