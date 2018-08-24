__author__ = 'oscarmora'
from django import forms
from .models import ProductRegister, ContactRegister, ProviderRegister

class ProductRegisterModelForm(forms.ModelForm):
    class Meta:
        model = ProductRegister
        fields = ["nombre", "descripcion","cantidad","ubicacion","proveedor", "email", "image"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        base , provider = email.split("@")
        dominio , extension = provider.split(".")

        # Validamos si la extension del correo es validad , para guardar la variable en BD
        if not "com" in extension:
            raise forms.ValidationError("Error al generar/agregar este campo. No es un correo valido.")
         #"default@error.com"
        return email

class ContactRegisterModelForm(forms.ModelForm):

    class Meta:
        model = ContactRegister
        fields = ["nombre", "mensaje", "email"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        base , provider = email.split("@")
        dominio , extension = provider.split(".")

        # Validamos si la extension del correo es validad , para guardar la variable en BD
        if not "com" in extension:
            raise forms.ValidationError("Error al generar/agregar este campo. No es un correo valido.")
         #"default@error.com"
        return email


class ProviderRegisterModelForm(forms.ModelForm):

    class Meta:
        model = ProviderRegister
        fields = ["nombre", "rfc", "direccion", "productos","cantidad", "punto_reorden"]

    def clean_rfc(self):
        rfc = self.cleaned_data.get("rfc")
        return rfc
