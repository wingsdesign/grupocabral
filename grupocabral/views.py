# -*- Mode: Python; coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext, Context
from django.template.loader import get_template
from django.core.mail import EmailMessage, send_mail, BadHeaderError, EmailMultiAlternatives
from django.db.models import Avg, Count, Q
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from django.urls import reverse
from django import forms
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
#import requests
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from rest_framework import viewsets

from grupocabral.filiais.models import Filias, Foto
from grupocabral.noticias.models import Noticia, Comentario
from grupocabral.noticias.forms import ComentarioForm

def HomeView(request):
    context = {}
    context["inicial_filiais"] = Filias.objects.all()
    return render(request, "index.html", context)

def RafaelCabral(request):
    context = {}
    return render(request, "rafael_cabral.html", context)

def GrupoCabral(request):
    context = {}
    return render(request, "grupo_cabral.html", context)

class NoticiaListView(ListView):
    model = Noticia
    paginate_by = 6
    template_name = 'blog.html'

    def get_context_data(self, *args, **kwargs):
        context = super(NoticiaListView, self).get_context_data(*args, **kwargs)
        context["resultado_filter"] = self.get_queryset().count()
        
        return context

    def get_queryset(self, *args, **kwargs):
        q = super(NoticiaListView, self).get_queryset(*args, **kwargs)
        busca_valor = self.request.GET.get('query', None)
        if busca_valor:
            return q.filter(Q(titulo__icontains=busca_valor) |
                            Q(categoria__nome__icontains=busca_valor))
        return q

class NoticiaDetailView(DetailView):
    model = Noticia
    context_object_name = 'object_lists'
    template_name = 'noticias_detalhes.html'

def noticias_detalhes(request, slug, *args, **kwargs):
    object_list = get_object_or_404(Noticia, slug=slug)
    single = Noticia.objects.get(slug=slug)

    object_list.noticia_views=object_list.noticia_views+1
    object_list.save()

    comentarios = object_list.comentarios.filter(active=True, resposta__isnull=True)
    if request.method == 'POST':
        comment_form = ComentarioForm(data=request.POST)
        if comment_form.is_valid():
            resposta_obj = None
        try:
            resposta_id = int(request.POST.get('resposta_id'))
        except:
            resposta_id = None
        if resposta_id:
            resposta_obj = Comentario.objects.get(id=resposta_id)
            if resposta_obj:
                reply_comment = comment_form.save(commit=False)
                reply_comment.resposta = resposta_obj
        new_comment = comment_form.save(commit=False)
        new_comment.comentario = object_list
        new_comment.save()
        return redirect('noticias:noticias_detalhes', slug)
    else:
        comment_form = ComentarioForm()

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

    return render(request, 'blog_detalhes.html', {'object_lists':object_list, 'comment_form':comentarios, 'comment_form':comment_form})




