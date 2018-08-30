from __future__ import unicode_literals

from django.db import models

class CategoryCatalogue(models.Model):
    class Meta:
        verbose_name_plural='CategoriesCatalogue'
    name = models.CharField(max_length=20, blank=False, null =False)
    categoryNumber = models.CharField(max_length=20, blank=False, null =False)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class ProductRegister(models.Model):
    id          = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nombre      = models.CharField(max_length=35, blank=True,null=True)
    descripcion = models.CharField(max_length=120, blank=True,null=True)
    cantidad_minima= models.IntegerField(default=0)
    #Cambiar a cantidad maxima o agregar otra para generar mas cantidades y el punto de reorden.
    cantidad    = models.IntegerField(default=0)
    punto_reorden= models.IntegerField(default=0)
    proveedor   = models.CharField(max_length=10, blank=True,null=True)
    email       = models.EmailField()
    #productCategory = models.ForeignKey(CategoryCatalogue)
    image = models.ImageField(upload_to='products/images',blank=True,null=True)
    ubicacion = models.CharField(max_length=10, blank=True, null=True)
    fechaIngreso = models.DateField(auto_now_add=True, auto_now=False)

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

