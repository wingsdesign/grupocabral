# -*- Mode: Python; coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.core.cache import cache
from django.dispatch import receiver
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from smtplib import SMTPAuthenticationError
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from model_utils.models import TimeFramedModel
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save, post_delete
from localflavor.br.br_states import STATE_CHOICES
from ckeditor_uploader.fields import RichTextUploadingField
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File
from datetime import date
from colorfield.fields import ColorField


class Filias(models.Model):
	filial = models.CharField(u'Filial', max_length=300)
	slug = models.SlugField(null=True, default=None, max_length=150, unique=True, db_index=True)
	site = models.URLField(u'WebSite', blank=True, null=True, help_text="se tiver site preencha so mente o link do site exe: <b>www.nomedosite.com.br</b>")
	logomarca = models.ImageField(u'Logomarca', upload_to='filiais', help_text="Notifique-se que o tamanho da Imagem é de <b>770x770</b>")
	informativo = RichTextUploadingField(u'Sobre a Empresa', blank=True, null=True)
	endereco = models.CharField(u'Endereço', max_length=300, blank=True)
	localizacao = models.CharField(u'Localização do Google', blank=True, max_length=500)
	valores = RichTextUploadingField(u'Nossos Valores', blank=True, null=True)
	visao = RichTextUploadingField(u'nossa visão', blank=True, null=True)
	missao = RichTextUploadingField(u'nossa missão', blank=True, null=True)
	slide1 = models.ImageField(u'Imagen Slide 1',upload_to='filiais/slid', null=True,  blank=True, help_text="Notifique-se que o tamanho da Imagem é de <b>868x614</b>")
	slide2 = models.ImageField(u'Imagen Slide 2',upload_to='filiais/slid', null=True,  blank=True, help_text="Notifique-se que o tamanho da Imagem é de <b>868x614</b>")
	slide3 = models.ImageField(u'Imagen Slide 3',upload_to='filiais/slid', null=True,  blank=True, help_text="Notifique-se que o tamanho da Imagem é de <b>868x614</b>")
	whatsapp = models.CharField(u'Whatsapp', blank=True, max_length=150)
	facebook = models.URLField(u'Facebook', blank=True, help_text='link do facebook')
	instagram = models.URLField(u'Instagram', blank=True, help_text='link do instagram')
	youtube = models.URLField(u'Youtube', blank=True, help_text='link do youtube')
	paleta_cor = ColorField(u'Paleta de Cor', default='#1e5b9c')
	filiais_views = models.IntegerField(u'Quatidade de Visualizações', default=0, blank=True)

	def fotos(self):
		if self.logomarca:
			return mark_safe("""<a href="/media/%s" target="_blank"><img src="/media/%s" width="60" height="60"></a>""" % (self.logomarca, self.logomarca))
		else:
			return "Imagem Indisponivel"
	fotos.allow_tags = True
	fotos.short_description = 'fotos'

	def get_absoulte_url(self):
		return reverse('filiais:filiais_detalhes', kwargs={"slug": self.slug}) 

	def __str__(self):
		return f"{self.filial}"

	class Meta:
		verbose_name = u'Uma Filial'
		verbose_name_plural =  u'FILIAIS'		

class Foto(models.Model):
    show = models.ForeignKey(Filias, on_delete=models.CASCADE, related_name="photos")
    imagen_filiais = models.ImageField(upload_to='filiais/imagens/')
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.show.filial

    class Meta:
        ordering = ["-data"]
        
    def fotos(self):
        if self.imagen_filiais:
            return mark_safe("""<a href="/media/%s" target="_blank"><img src="/media/%s" width="60" height="60"></a>""" % (self.imagen_filiais, self.imagen_filiais))
        else:
            return "Imagem Indisponivel"
    fotos.allow_tags = True
    fotos.short_description = 'fotos'

class Comentario(models.Model):
    comentario = models.ForeignKey(Filias , on_delete=models.CASCADE, related_name="comentarios")
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


