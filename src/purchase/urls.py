__author__ = 'oscarmora'

from django.conf.urls import url
from views import CreateQuoteView, ListQuoteView

urlpatterns =[
    url(r'^createQuote/$', CreateQuoteView.as_view(), name='createQuote'),
    url(r'^listQuote/$', ListQuoteView.as_view(), name='listQuote'),
]