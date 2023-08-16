# -*- Mode: Python; coding: utf-8 -*-
from django import forms
from django.contrib import admin
from .models import Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'data')
    save_on_top=True


admin.site.register(Contato, ContatoAdmin)


