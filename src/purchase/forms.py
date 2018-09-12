from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit,Div

from models import Quote

class QuoteModelForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ["quoteNumber", "creationDate", "row", "quantity","unity", "description","deliveryDate", "weight", "price", "rowTotal", "taxIVA", "quoteTotal", "creator"]
        labels ={
        'quoteNumber':'Folio',
        'creationDate':'Fecha de Creacion',
        'row':'Partida',
        'quantity':'Cantidad',
        'unity':'Unidad',
        'description':'Descripcion',
        'deliveryDate':'Fecha de Entrega',
        'weight':'Peso',
        'price':'Precio',
        'rowTotal':'Subtotal',
        }
    def __init__(self, *args, **kwargs):
        super(QuoteModelForm,self).__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_QuoteModel_form'
        self.helper.form_method = 'POST'
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Div(
                Div('row',css_class='col-sm-1'),
                Div('quantity',css_class='col-sm-1'),
                Div('unity',css_class='col-md-1'),
                Div('weight',css_class='col-md-1'),
                Div('description',css_class='col-md-4'),
                Div('price',css_class='col-md-2'),
                Div('rowTotal',css_class='col-md-2'), css_class = 'row'
            )
        )