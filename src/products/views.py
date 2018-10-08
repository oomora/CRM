from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
# Agregamos las forma y el modelo para poder darle a la vista la informacion de las rutas de acceso
from .forms import ContactRegisterModelForm, ProductRegisterModelForm, ProviderRegisterModelForm
from .models import ProductRegister, ProviderRegister, ContactRegister, CategoryCatalogue

#Pagination for the products
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.views import status

import json


def index(request):
    # Validar que el usuario este autenticado
    #if request.user == user.is_authenticated():
        #title = "Bienvenido %s" %(request.user)
    #else:
    title = " :: Product Creation Page ::"
    form = ProductRegisterModelForm(request.POST or None)
    # Methodo is_valid() para generar correctamente el diccionario de datos de la forma
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Product saved succesfully!')
        return redirect( 'index')
    else:
        contexto = {
            "title": title,
            "form": form,
        }
        #messages.error(request, 'Product with errors, instance not saved!')
        return render(request, 'index.html', contexto)



def contact(request):
    title = " :: CRM Contact Page ::"
    form = ContactRegisterModelForm(request.POST or None)
    if form.is_valid():
        nombre = form.cleaned_data.get("nombre")
        mensaje = form.cleaned_data.get("mensaje")
        email = form.cleaned_data.get("email")
        #print "nombre: ",nombre," mensaje: ", mensaje , " email: ",email

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    contexto = {
            "title": title,
            "contactForm": form,
        }

    return render(request, 'contact.html', contexto)

def provider(request):
    title = ":: CRM Provider ::"
    form = ProviderRegisterModelForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    contexto ={
        "title": title,
        "providerForm": form,
    }
    return render(request, 'provider.html',contexto)

def search(request):
    title = ":: List Products Page ::"

    productos = ProductRegister.objects.all().order_by("id")
    paginator = Paginator(productos, 10)

    page = request.GET.get('page')

    try:
        productos = paginator.page(page)
    except PageNotAnInteger:
        # raise PageNotAnInteger('Pagina no es un numero, generamos la el primer objeto de la pagina')
        productos = paginator.page(1)
    except EmptyPage:
        # raise EmptyPage('No existen registros asociados a la pagina solicitada')
        productos = paginator.page(paginator.num_pages)

    contexto= {
        "title" : title,
        "productos": productos,
    }
    return render(request, 'search.html', contexto)

def searchProvider(request):
    title = ":: CRM List Provider page ::"
    proveedores = ProviderRegister.objects.all().order_by("id")

    contexto= {
        "title" : title,
        "proveedores": proveedores,
    }
    return render(request, 'searchProvider.html', contexto)

def searchContacts(request):
    title = ":: CRM List Contacts page ::"
    contactos = ContactRegister.objects.all().order_by("id")

    contexto= {
        "title" : title,
        "contactos": contactos,
    }
    return render(request, 'searchContacts.html', contexto)


def edit(request, id):
    title = ":: CRM Edit page ::"
    producto = ProductRegister.objects.get(id=id)

    if request.method == 'GET':
        form = ProductRegisterModelForm(instance=producto)
    else:
        form = ProductRegisterModelForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('search')
    contexto= {
                "title" : title,
                "producto": producto,
                "form": form,
    }
    return render(request, 'edit.html', contexto)

def delete(request, id):
    title = ":: CRM Delete page ::"
    producto = ProductRegister.objects.get(id=id)

    if request.method == 'POST':
        producto.delete()
        return redirect('search')

    return render(request, 'delete.html', {'producto':producto})