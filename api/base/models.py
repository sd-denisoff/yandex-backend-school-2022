from django.db import models
from django.utils.translation import gettext_lazy as _


class Item(models.Model):
    class ItemType(models.TextChoices):
        OFFER = 'O', _('Offer')
        CATEGORY = 'C', _('Category')

    id = models.CharField(max_length=256, primary_key=True)
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=1, choices=ItemType.choices)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, null=True)
    price = models.IntegerField(null=True)
    date = models.DateTimeField()

    def __str__(self):
        return f'Item {self.name} of type {self.type}'
