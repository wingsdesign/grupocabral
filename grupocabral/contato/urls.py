from django.urls import re_path, path, include

from .views import ContatoCreate, ContatoCreateSuccess

app_name = 'contato'

urlpatterns = [
    path('contato/', ContatoCreate.as_view(), name='contato_form'),
    path('contato/sucesso/', ContatoCreateSuccess.as_view(), name='contato_form_success'),
]
