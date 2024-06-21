from django.db import models
from simple_history.models import HistoricalRecords

class Product(models.Model):
    name = models.CharField(max_length=32)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    price = models.FloatField()
    is_selling = models.BooleanField()
    is_missing = models.BooleanField()
    out_of_stock = models.BooleanField()
    expiry_date = models.DateField()
    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        # Clear any necessary cache or perform additional updates here

    def __str__(self):
        return self.name
    
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value