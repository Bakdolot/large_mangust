from django.db import models


class Order(models.Model):
    customer = models.CharField(max_length=255, db_index=True)
    item = models.CharField(max_length=255, db_index=True)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField()
