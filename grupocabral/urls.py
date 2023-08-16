# -*- Mode: Python; coding: utf-8 -*-
from django.contrib.auth.decorators import permission_required
from django.conf.urls import *
from django.contrib import admin
from django.urls import re_path, path, include
from django.contrib.staticfiles import views
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.conf import settings

from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from rest_framework.views import APIView
from grupocabral.views import *
from . import views

urlpatterns = [
    path('', HomeView, name="HomeView"),
    path('rafael-cabral/', RafaelCabral, name="RafaelCabral"),
    path('grupo-cabral/', GrupoCabral, name="GrupoCabral"),
    path('blog/', include("grupocabral.noticias.urls", namespace="noticias")),
    path('', include('grupocabral.contato.urls', namespace='contato')),
    path('filiais/', include('grupocabral.filiais.urls', namespace='filiais')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)