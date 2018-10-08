from __future__ import unicode_literals

from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Quote(models.Model):
    class Meta:
        verbose_name_plural='Quotes'

    id = models.AutoField(primary_key=True)
    quoteNumber = models.IntegerField(default=0)
    #provider = models.CharField() -- Actualizar con la lista de proveedores para elegir al que corresponde.
    creationDate = models.DateField(default=timezone.now, blank=False)
    row = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    unity = models.CharField(default='Pieza', max_length=12)
    description = models.CharField(default='Descripcion del articulo', max_length=30)
    deliveryDate = models.DateField(default=timezone.now)
    weight = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    rowTotal = models.IntegerField(default=0)
    taxIVA = models.IntegerField(default=16)
    quoteTotal = models.IntegerField(default=0)
    creator = models.CharField(default='OMP', max_length=30)

    def __unicode__(self):
        return self.description

    def __str__(self):
       return self.description