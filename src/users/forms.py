__author__ = 'oscarmora'

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields =[
                'username',
                'first_name',
                'last_name',
                'email',
        ]
        labels ={
            'username': 'Nombre Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo',
        }
