from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Product
from datetime import date

@admin.register(Product)
class ProductAdmin(SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ('name', 'code', 'price', 'is_selling', 'is_missing', 'out_of_stock', 'expiry_date', 'expired_status')

    def expired_status(self, obj):
        return date.today() > obj.expiry_date
    
    expired_status.boolean = True
    expired_status.short_description = 'Expired'