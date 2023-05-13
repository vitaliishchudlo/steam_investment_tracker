from django.contrib import admin

from .models import Skin

#
class SkinAdmin(admin.ModelAdmin):
    list_display = (
    'name', 'price_per_item', 'item_count', 'items_total', 'current_price', 'created_date', 'modified_date')
    # readonly_fields = ('items_total',)
    #
    # def items_total(self, obj):
    #     return obj.items_total()
    #
    # items_total.short_description = 'Total'


admin.site.register(Skin, SkinAdmin)
