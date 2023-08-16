from django import forms
from django.core.validators import validate_image_file_extension
from django.utils.translation import gettext as _
from localflavor.br.forms import BRCPFField
from localflavor.br.br_states import STATE_CHOICES

from .models import Filias, Comentario, Foto

class FilialForm(forms.ModelForm):
    class Meta:
        model = Filias
        fields = ('__all__')

    photos = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        label=("ADICIONAR FOTOS DO PROJETO"),
        required=False,
    )

    def clean_photos(self):
        for upload in self.files.getlist("photos"):
            validate_image_file_extension(upload)

    def save_photos(self, show, *args, **kwargs):
        for upload in self.files.getlist("photos"):
            photo = Foto(show=show, imagen_filiais=upload)
            photo.save()


class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ('usuario', 'texto',  'email')
