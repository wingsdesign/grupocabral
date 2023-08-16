# -*- Mode: Python; coding: utf-8 -*-
from django.urls import re_path, path
from django.contrib import admin
from grupocabral.views import *
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.conf import settings

from . import views

app_name = 'noticias'

urlpatterns = [
    path('',NoticiaListView.as_view(), name='lista_noticias'),
    path('<slug:slug>/',noticias_detalhes, name='noticias_detalhes'),
]