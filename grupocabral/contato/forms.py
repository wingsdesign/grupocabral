from django import forms

from localflavor.br.forms import BRCPFField
from localflavor.br.br_states import STATE_CHOICES

from .models import Contato


class ContatoForm(forms.ModelForm):

    class Meta:
        model = Contato
        fields = ('nome',  'email', 'telefone', 'assunto', 'mensagem')