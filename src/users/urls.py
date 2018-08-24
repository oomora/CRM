__author__ = 'oscarmora'

from django.conf.urls import url
from views import UserCreateView

urlpatterns =[
    url(r'^create', UserCreateView.as_view(), name='createUser'),
]