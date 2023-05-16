from django.contrib import admin
from .models import Skin

from django.utils import timezone

class SkinAdmin(admin.ModelAdmin):
    # The table in the admin menu -> http://127.0.0.1:8000/admin/skins_tables/skin/
    list_display = ('name', 'item_count', 'price_per_item', 'current_price', 'created_date', 'modified_date')
    # Added fields in the item view -> http://127.0.0.1:8000/admin/skins_tables/skin/44/change/
    # readonly_fields = ('modified_date',)
    fields = ('name', 'price_per_item', 'item_count','created_date')


admin.site.register(Skin, SkinAdmin)


