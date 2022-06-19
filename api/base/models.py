from django.db import models
from django.utils.translation import gettext_lazy as _


class Item(models.Model):
    class ItemType(models.TextChoices):
        OFFER = 'O', _('OFFER')
        CATEGORY = 'C', _('CATEGORY')

    id = models.CharField(max_length=256, primary_key=True)
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=10, choices=ItemType.choices)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, null=True)
    price = models.IntegerField(null=True)
    date = models.CharField(max_length=32)

    def __str__(self):
        return f'Item {self.name} of type {self.type}'
