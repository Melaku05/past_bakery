from django.contrib import admin
from django.utils.html import format_html
from .models import Paywithbank, Bankname
from msigana_ecommerce.admin_site import admin_site

class BankNameFilter(admin.SimpleListFilter):
    title = 'Bank Name'
    parameter_name = 'bank_name'

    def lookups(self, request, model_admin):
        bank_names = Paywithbank.objects.values_list('bank_name', flat=True).distinct()
        return [(name, name) for name in bank_names]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(bank_name=self.value())
        return queryset

class PaywithbankAdmin(admin.ModelAdmin):
    list_display = ('transaction_no', 'payment_status', 'bank_name', 'ref_number', 'phone_number', 'total_amount', 'paid_by_bank', 'payment_date', 'display_screenshot_thumbnail')
    list_filter = (BankNameFilter,)
    readonly_fields = ('transaction_no', 'payment_status', 'bank_name', 'ref_number', 'phone_number', 'total_amount', 'paid_by_bank', 'payment_date', 'user_bank_account_name')

    search_fields = ('user__username', 'bank_name')

    def display_screenshot_thumbnail(self, obj):
        if obj.screenshot:
            return format_html('<img src="{}" width="50" height="auto" />', obj.screenshot.url)
        else:
            return 'No Image'

    display_screenshot_thumbnail.short_description = 'Thumbnail'

    def display_screenshot_url(self, obj):
        if obj.screenshot:
            return format_html('<a href="{}" target="_blank">{}</a>', obj.screenshot.url, 'View Image')
        else:
            return 'No Image'

    display_screenshot_url.short_description = 'Screenshot URL'

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False




class BanknameAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name','account')

admin_site.register(Bankname, BanknameAdmin)
admin_site.register(Paywithbank, PaywithbankAdmin)
