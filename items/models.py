from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)
    item_type = models.CharField(max_length=50)
    rarity = models.CharField(max_length=20)
    attunement = models.BooleanField()
    notes = models.CharField(max_length=500)

    def __str__(self):
        return str(self.name)
