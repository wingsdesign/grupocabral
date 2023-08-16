# -*- Mode: Python; coding: utf-8 -*-
from django.conf.urls import *
from django.contrib import admin
from grupocabral.views import *
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.conf import settings
from django.urls import re_path, path, include


from .views import FilialListView, FilialDetalhesView
from . import views
app_name = 'filiais'

urlpatterns = [
	path('', FilialListView.as_view(), name='filiais_list'),
	path('<slug:slug>/',FilialDetalhesView, name='filiais_detalhes'),
	
]