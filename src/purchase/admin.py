from django.contrib import admin

from models import Quote
from forms import QuoteModelForm

# Register your models here.
class AdminQuotes(admin.ModelAdmin):
    list_display =["quoteNumber", "row", "quantity", "unity", "description", "rowTotal"]
    search_fields = ('quoteNumber', 'row')
    form = QuoteModelForm

admin.site.register(Quote, AdminQuotes)
