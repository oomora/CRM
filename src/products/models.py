from __future__ import unicode_literals

from django.db import models
#from .models import CategoryCatalogue

class CategoryCatalogue(models.Model):
    class Meta:
        verbose_name_plural='CategoriesCatalogue'

    category_number = models.CharField(max_length=5, blank=False, null=False, primary_key=True)
    category_name = models.CharField(max_length=30, blank=False, null=False)
    category_status = models.CharField(default="ACTIVE", max_length=10, blank=False, null=False)

    def __unicode__(self):
        return self.category_name

    def __str__(self):
        return self.category_name

class ProductRegister(models.Model):
    #id          = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nombre      = models.CharField(max_length=35, blank=True,null=True)
    descripcion = models.CharField(max_length=120, blank=True,null=True)
    cantidad_minima= models.IntegerField(default=0)
    #Cambiar a cantidad maxima o agregar otra para generar mas cantidades y el punto de reorden.
    cantidad_maxima    = models.IntegerField(default=0)
    punto_reorden= models.IntegerField(default=0)
    proveedor   = models.CharField(max_length=30, blank=True,null=True)
    #email       = models.EmailField()
    categoria = models.ForeignKey(CategoryCatalogue,on_delete=None, null=True, blank=False)
    sku = models.CharField(default='NA', max_length=25, blank=True, null=False)
    image = models.ImageField(upload_to='products/images',blank=True,null=True)
    ubicacion = models.CharField(max_length=10, blank=True, null=True)
    fecha_ingreso = models.DateField()

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre

class ProviderRegister(models.Model):
    nombre      = models.CharField(max_length=120,blank=True,null=True)
    rfc         = models.CharField(max_length=20,blank=True,null=True)
    direccion   = models.CharField(max_length=120)
    productos   = models.CharField(max_length=120)
    cantidad    = models.IntegerField()
    punto_reorden = models.IntegerField(default=0)

    def __unicode__(self):
        return self.rfc

    def __str__(self):
        return self.rfc

class ContactRegister(models.Model):
    nombre = models.TextField(max_length=30, blank=True,null=True)
    mensaje = models.TextField(max_length=100, blank=True,null=True)
    email = models.EmailField()

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre

class OrderCatalogue(models.Model):
    nombre = models.CharField(max_length=20, blank=False, null =False)
    label = models.CharField(max_length=20, blank=False, null =False)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre

