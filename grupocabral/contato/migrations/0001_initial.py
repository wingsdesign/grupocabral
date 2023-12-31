# Generated by Django 4.0.4 on 2023-08-13 12:11

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255, verbose_name='Nome Completo')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(blank=True, max_length=255)),
                ('telefone', models.CharField(blank=True, help_text='Informe o Celular com o DDD, <b>Ex: (99) 99999-9999</b>', max_length=20, verbose_name='Celular')),
                ('assunto', models.CharField(blank=True, max_length=255, verbose_name='Assunto')),
                ('mensagem', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Mensagem')),
                ('email_sent', models.BooleanField(default=False, verbose_name='email sent')),
            ],
            options={
                'verbose_name': 'Um Contato',
                'verbose_name_plural': 'Contato',
                'ordering': ['-id'],
            },
        ),
    ]
