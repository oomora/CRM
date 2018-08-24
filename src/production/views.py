from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from models import Activity
from django.core.urlresolvers  import reverse_lazy
from forms import *

# Create your views here.
class ActivityList(ListView):
    model= Activity
    template_name = 'search.html'

class ActivityCreate(CreateView):
    model = Activity
    form_class = ActivityForm
    template_name= 'production.html'
    success_url = reverse_lazy('activityCreate')