# models.py
from django.db import models

class RiskData(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    rate = models.FloatField()
    def __str__(self):
        return self.name