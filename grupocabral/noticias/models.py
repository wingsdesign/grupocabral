# -*- Mode: Python; coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from .validators import file_size
from django.utils.text import slugify
from PIL import Image

from django.utils.safestring import mark_safe

import sys

class Noticia(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(u'Título da Postagem', max_length=300)
    slug = models.SlugField(blank=True, null=True, default=None, max_length=300,
    unique=True, db_index=True)
    imagen = models.ImageField(u'Imagem da Postagem', upload_to='noticia',
    help_text="Notifique-se que o tamanho da Imagem é de. <b>Ex: 984X655</b>")
    data = models.DateTimeField()
    descricao = RichTextUploadingField(u'Sua Postagem', blank=True)
    noticia_views = models.IntegerField(u'Quatidade de Visualizações', default=0, blank=True)
    def get_absoulte_url(self):
        return reverse('noticia:noticias_detalhes', kwargs={"slug": self.slug}) 

    def __str__(self):
        return self.titulo

    def fotos(self):
        if self.imagen:
            return mark_safe("""<a href="/media/%s" target="_blank"><img src="/media/%s" width="60" height="40"></a>""" % (self.imagen, self.imagen))
        else:
            return "Imagem Indisponivel"
    fotos.allow_tags = True
    fotos.short_description = 'fotos'

    class Meta:
        verbose_name = u'UMA NOTÍCIA'
        verbose_name_plural = u'NOTÍCIAS'
        ordering = ['-data']

class Comentario(models.Model):
    comentario = models.ForeignKey(Noticia , on_delete=models.CASCADE, related_name="comentarios")
    usuario = models.CharField(u'Usuário', max_length=250)
    email = models.EmailField()
    texto = models.TextField()
    data_criada = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    resposta = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="respostas")

    class Meta:
        verbose_name, verbose_name_plural = u"UM COMENTÁRIO" , u"COMENTÁRIO"
        ordering = ['-data_criada']

    def __str__(self):
        return self.usuario


