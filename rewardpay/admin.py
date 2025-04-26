from django.contrib import admin
from .models import RewardRate, PaywithReward
from msigana_ecommerce.admin_site import admin_site

class RewardRateAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if RewardRate.objects.exists():
            return False
        return super().has_add_permission(request)


class PaywithRewardAdmin(admin.ModelAdmin):

   
    list_display = ['user', 'total_amount', 'payment_date', 'payment_status']
    list_filter = ['payment_date', 'payment_status']
    search_fields = ['user', 'total_amount', 'payment_date', 'payment_status']
    readonly_fields = ['transaction_no','user', 'total_amount', 'payment_date', 'payment_status']
    list_per_page = 30

    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
        

admin_site.register(RewardRate, RewardRateAdmin)
admin_site.register(PaywithReward, PaywithRewardAdmin)