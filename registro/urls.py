# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from registro import views
from registro.views import *
from django.conf import settings


urlpatterns = patterns('',
    url(r'^$', views.List_files.as_view(), name='list_files'),
    url(r'^file$', views.file, name='file'),
    # Definiendo la url que va a servir los archivos/documentos para que puedan ser descargados.
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
    url(r'^busqueda/media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
    url(r'^buscar/$', buscar, name='buscar'),
    url(r'^busqueda/$', busqueda, name='busqueda'),
)
