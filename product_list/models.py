from django.db import models
from .utils import get_current_gold_price 
# Create your models here.



class Product(models.Model):
    name = models.CharField(max_length=50)
    popularity_score = models.FloatField()
    weight = models.FloatField()
    images = models.JSONField()
    price = models.FloatField(blank=True,null=True)

    def __str__(self):
        return self.name
    

    def save(self, *args, **kwargs):
        gold_price = get_current_gold_price()
        self.price = (self.popularity_score + 1) * self.weight * gold_price
        super().save(*args, **kwargs)
