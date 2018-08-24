
from django.contrib.auth.models import User
from django.views.generic import CreateView

from django.core.urlresolvers import reverse_lazy

from forms import UserCreateForm

# Create your views here.
class UserCreateView(CreateView):
    model = User
    template_name = 'user.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')