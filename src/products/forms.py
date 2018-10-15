__author__ = 'oscarmora'
from django import forms
from .models import ProductRegister, CategoryCatalogue, ContactRegister, ProviderRegister

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit,Div, Field

class ProductRegisterModelForm(forms.ModelForm):
    class Meta:
        model = ProductRegister
        fields = ["nombre", "descripcion","cantidad_minima","cantidad_maxima","punto_reorden",
                  "ubicacion","sku", "fecha_ingreso","categoria", "image"]


    def __init__(self, *args, **kwargs):
        super(ProductRegisterModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_tag = True
        self.helper.form_action = 'index'
        #self.helper.form_class = 'form-inline'
        self.helper.layout = Layout(
            Div(
                Div('nombre', css_class='col-sm-5'),
                Div('descripcion', css_class='col-sm-5'),
                Div('categoria', css_class='col-md-2'), css_class='row'
            ),
            Div(
                Div('cantidad_minima', css_class='col-sm-2'),
                Div('cantidad_maxima', css_class='col-sm-2'),
                Div('punto_reorden', css_class='col-sm-2'),
                Div('ubicacion', css_class='col-md-2'),
                #Div('proveedor', css_class='col-md-2')
                Div('fecha_ingreso', css_class='col-md-2', css_id='fecha_ingreso'),
                Div('sku', css_class='col-md-2'), css_class='row'
            ),
            Div(
                Div('image', css_class='col-md-2'), css_class='row'
            ),
            Div(
                Submit('submit', 'Enviar', css_class='btn btn-default')
            )
        )

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
