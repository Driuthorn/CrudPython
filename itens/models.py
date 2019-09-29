from django.db import models

class Itens(models.Model):
    name = models.CharField(max_length=100, blank=False)
    price = models.FloatField(blank=False)
    description = models.TextField(max_length=150, blank=True)

    def __str__(self):
        return self.name
