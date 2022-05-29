from django.db import models

# Create your models here.

class Good(models.Model):
    name = models.TextField(null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(default=0)
    qty = models.TextField(null=True, blank=True)
    distributor = models.TextField(null=True, blank=True)