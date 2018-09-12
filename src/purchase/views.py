from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView

from models import Quote

from django.core.urlresolvers  import reverse_lazy
from forms import QuoteModelForm

class ListQuoteView(ListView):
    model = Quote
    template_name = 'listQuoteForm.html'

# Create your views here.
class CreateQuoteView(CreateView):
    model = Quote
    form_class = QuoteModelForm
    template_name= 'createQuoteForm.html'
    success_url = reverse_lazy('createQuote')


