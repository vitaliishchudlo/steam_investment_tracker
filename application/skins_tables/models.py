from django.db import models
from decimal import Decimal
from django.utils import timezone

class Skin(models.Model):
    name = models.CharField(max_length=100)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2)
    item_count = models.IntegerField()
    current_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
