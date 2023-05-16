from django.db import models
from decimal import Decimal

class Skin(models.Model):
    name = models.CharField(max_length=100)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2)
    item_count = models.IntegerField()
    current_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    # @property
    # def items_total(self):
    #     return Decimal(str(self.price_per_item)) * Decimal(str(self.item_count))
    #
    # @property
    # def current_items_total(self):
    #     return Decimal(str(self.current_price)) * Decimal(str(self.item_count))

    def __str__(self):
        return self.name
