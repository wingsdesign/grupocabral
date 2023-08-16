# -*- Mode: Python; coding: utf-8 -*-
from django.contrib import admin
from .models import Noticia, Comentario

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'data',  'fotos']
    search_fields = ['titulo']
    prepopulated_fields = {'slug' : ('titulo',)}
    save_on_top=True
    
    def format_date(self, obj):
        return obj.data.strftime('%b, %Y')

    format_date.admin_order_field = 'data'
    format_date.short_description = 'Data'

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'email', 'data_criada', 'active']


admin.site.site_header = u"GRUPO CABRAL"
admin.site.index_title = u"Administração do Site"
admin.site.site_title = u"GRUPO CABRAL"


admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Comentario, ComentarioAdmin)
