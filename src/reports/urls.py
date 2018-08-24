__author__ = 'oscarmora'

from django.conf.urls import url
from views import UserReport

urlpatterns =[
    url(r'^reportProducts',UserReport, name='reportProducts'),
]