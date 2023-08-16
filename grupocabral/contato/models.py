# -*- Mode: Python; coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.core.cache import cache
from django.dispatch import receiver


from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from localflavor.br.br_states import STATE_CHOICES
from django.utils.html import format_html
from smtplib import SMTPAuthenticationError
from django.core.mail import send_mail
from django.conf import settings


class Contato(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(u'Nome Completo', max_length=255)
    data = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=255, blank=True)
    telefone = models.CharField(u'Celular', max_length=20, blank=True, help_text='Informe o Celular com o DDD, <b>Ex: (99) 99999-9999</b>')
    assunto = models.CharField(u'Assunto', blank=True, max_length=255)
    mensagem = RichTextUploadingField(u'Mensagem', blank=True)
    email_sent = models.BooleanField(u'email sent', default=False)


    class Meta:
        verbose_name = u'Um Contato'
        verbose_name_plural =  u'Contato'
        ordering = ['-id']

    def __str__(self):
        return u"%s" % self.nome
        
    def send_email(self):
        message_admin = """
        Nova Mensagem - Grupo Cabral
        Nome: {0}
        Email: {1}
        Telefone: {2}
        Assunto: {3}

        Mensagem: {4}

        """
        message_admin = message_admin.format(self.nome,self.email, self.telefone, self.assunto, self.mensagem)

        message = """
Ola {0},
Obrigado por entrar em contato conosco.

Nossa equipe de atendimento responderá o mais breve possível.
        """
        message = message.format(self.nome)

        try:
            send_mail(
                'Novo Contato | Grupo Cabral',
                message_admin,
                'Grupo Cabral <contato@grupocabral.com.br>',
                settings.ADMINS,
                fail_silently=False,
            )
            send_mail(
                'Auto Mensagem - Grupo Cabral',
                message,
                'Grupo Cabral <contato@grupocabral.com.br>',
                [self.email],
                html_message=message,
                fail_silently=False,
            )
            self.email_sent = True
            self.save()
        except smtplib.SMTPAuthenticationError:
            pass


def send_confirmation_email(sender, instance, created, **kwargs):
    if not instance.email_sent:
        instance.send_email()


models.signals.post_save.connect(
    send_confirmation_email, sender=Contato, dispatch_uid='contato.Record')
