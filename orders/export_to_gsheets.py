import gspread
from oauth2client.service_account import ServiceAccountCredentials
from .models import Order, OrderItem
import os
from django.conf import settings

# Construct an absolute path to the credentials file
creds_file = os.path.join(settings.BASE_DIR, 'orders', 'credentials', 'tanabelesorder.json')
def export_orders_to_gsheets(queryset):
    # Use the path to your JSON key file
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
    client = gspread.authorize(creds)
    # Open the Google Sheet
    sheet = client.open("tanabelesOrders").sheet1

    # Get your Order data
    orders = Order.objects.all()

    # Write the Order data to the Google Sheet
    for i, order in enumerate(orders, start=2):
        order_items = OrderItem.objects.filter(order=order)
        order_items_str = ', '.join([f'{item.product_name} ({item.quantity})' for item in order_items])
        sheet.update_cell(i, 1, order.first_name)
        sheet.update_cell(i, 2, order.last_name)
        sheet.update_cell(i, 3, order.order_phone)
        sheet.update_cell(i, 4, order.order_username)
        sheet.update_cell(i, 5, order.order_date.strftime('%Y-%m-%d'))
        sheet.update_cell(i, 7, order.order_address)
        sheet.update_cell(i, 9, order.status)
        sheet.update_cell(i, 10, order_items_str)