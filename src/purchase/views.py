from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView

from models import Quote

from django.core.urlresolvers  import reverse_lazy
from forms import QuoteModelForm

class ListQuoteView(ListView):
    model = Quote
    queryset = Quote.objects.all()
    context_object_name = 'quotes'
    template_name = 'listQuoteForm.html'

# Create your views here.
class CreateQuoteView(CreateView):
    model = Quote
    form_class = QuoteModelForm
    template_name= 'createQuoteForm.html'
    success_url = reverse_lazy('listQuote')

    def form_valid(self, form):
        model = form.save(commit=True)
        return super(CreateQuoteView, self).form_valid(form)

    def form_invalid(self, form):
        print 'Entramos al in-valid form'
        return self.render_to_response(self.get_context_data(form=form))