from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from localflavor.br.forms import BRCPFField
from localflavor.br.br_states import STATE_CHOICES

from .models import Comentario, Noticia

class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ('usuario', 'texto',  'email')

