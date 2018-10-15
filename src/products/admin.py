from django.contrib import admin

from .forms import ProductRegisterModelForm, ContactRegisterModelForm, ProviderRegisterModelForm
from .models import ProductRegister, ContactRegister, ProviderRegister, CategoryCatalogue


class AdminProductRegister(admin.ModelAdmin):
    list_display =  ["nombre", "descripcion", "cantidad_minima","cantidad_maxima", "ubicacion",
                     "sku", "fecha_ingreso","categoria", "image"]
    search_fields = ('nombre', 'descripcion')
    form = ProductRegisterModelForm

class AdminContactRegister(admin.ModelAdmin):
    list_display =["nombre", "mensaje", "email"]
    search_fields = ('nombre', 'email')
    form = ContactRegisterModelForm

class AdminProviderRegister(admin.ModelAdmin):
    list_display =["nombre", "rfc", "direccion", "productos", "cantidad", "punto_reorden"]
    search_fields = ('nombre', 'rfc')
    form = ProviderRegisterModelForm

class AdminCategoryCatalogue(admin.ModelAdmin):
    list_display = ["category_number","category_name"]

admin.site.register(ProductRegister, AdminProductRegister)
admin.site.register(ContactRegister, AdminContactRegister)
admin.site.register(ProviderRegister, AdminProviderRegister)
admin.site.register(CategoryCatalogue, AdminCategoryCatalogue)


