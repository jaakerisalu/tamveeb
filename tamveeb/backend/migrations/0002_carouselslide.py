# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import backend.models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselSlide',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Pealkiri')),
                ('content', models.TextField(verbose_name='Sisu', help_text="Sisu kasutatakse kui HTML-i, võid kasutada linke: (<a class='yyy' href='xxx' target='_blank'>Link</a>) jne")),
                ('link', models.CharField(max_length=20, verbose_name='Nupu link', choices=[('muusika', 'Muusika'), ('meist', 'Meist'), ('kontakt', 'Kontakt'), ('lisaleht', 'Lisaleht')], help_text='Mis lehele meie saidil antud slaid viitab')),
                ('anchor', models.CharField(max_length=255, verbose_name='Nupu lingi ankur', null=True, help_text='Kui tahad et link viiks mõne lehel asuva ankru juurde, siis kirjuta see siia', blank=True)),
                ('image', models.ImageField(upload_to=backend.models.random_carousel_image_path, verbose_name='Pilt')),
            ],
        ),
    ]
