# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-29 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0033_auto_20170629_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=500, null=True, verbose_name='Identificador'),
        ),
    ]