from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.
class Quote(models.Model):
    class Meta:
        verbose_name_plural='Quotes'

    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    quoteNumber = models.IntegerField(default=0)
    #provider = models.CharField() -- Actualizar con la lista de proveedores para elegir al que corresponde.
    creationDate = models.DateField(default=datetime.datetime.now())
    row = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    unity = models.CharField(default='Pieza', max_length=12)
    description = models.CharField(default='Descripcion del articulo', max_length=30)
    deliveryDate = models.DateField(default=datetime.datetime.now())
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