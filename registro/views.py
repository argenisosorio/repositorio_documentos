# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from registro.models import Document
from registro.forms import DocumentForm
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect


def file(request):
    """
    Función que permite guardar los documentos, se guardar en /media
    """
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('registro:list_files')
    else:
        form = DocumentForm()
    return render(request, 'registro/file.html', {
        'form': form
    })


class List_files(ListView):
    """
    Clase que permite listar los documentos registrados
    """
    model = Document
    template_name = "registro/list_files.html"


def buscar(request):
    """
    Función que muestra la plantilla con el formulario de búsqueda.
    """
    return render(request, 'registro/buscar.html')


def busqueda(request):
    """
    Función que permite hacer el query con los objetos ya filtrados.
    """
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        documents = Document.objects.filter(description__icontains=q)
        return render(request, 'registro/buscar.html',  {'documents': documents, 'query': q})
    else:
        return HttpResponse('Por favor introduce un termino de búsqueda.')
