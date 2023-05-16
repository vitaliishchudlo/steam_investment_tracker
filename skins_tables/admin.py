from django.contrib import admin
from .models import Skin

# class SkinAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price_per_item', 'item_count', 'get_items_total', 'current_price', 'created_date', 'modified_date')
#     readonly_fields = ('created_date', 'modified_date')
#
#     def get_items_total(self, obj):
#         return obj.items_total
#     get_items_total.short_description = 'Items Total'
#
#     # Override the default behavior of the created_date field
#     def get_exclude(self, request, obj=None):
#         if obj:  # Existing object
#             return ()  # Exclude no fields for existing objects
#         return ('created_date',)  # Exclude created_date for new objects

admin.site.register(Skin)


# from django.contrib import admin
#
# from .models import Skin
#
# #
# class SkinAdmin(admin.ModelAdmin):
#     list_display = (
#     'name', 'price_per_item', 'item_count', 'items_total', 'current_price', 'created_date', 'modified_date')
#     # readonly_fields = ('items_total',)
#     #
#     # def items_total(self, obj):
#     #     return obj.items_total()
#     #
#     # items_total.short_description = 'Total'
#
#
# admin.site.register(Skin, SkinAdmin)
