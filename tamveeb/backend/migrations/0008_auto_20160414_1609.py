# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_additionalpage_visible'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutustextblock',
            name='content_en',
            field=models.TextField(null=True, verbose_name='Sisu'),
        ),
        migrations.AddField(
            model_name='aboutustextblock',
            name='content_et',
            field=models.TextField(null=True, verbose_name='Sisu'),
        ),
        migrations.AddField(
            model_name='aboutustextblock',
            name='title_en',
            field=models.CharField(null=True, verbose_name='Pealkiri', max_length=255),
        ),
        migrations.AddField(
            model_name='aboutustextblock',
            name='title_et',
            field=models.CharField(null=True, verbose_name='Pealkiri', max_length=255),
        ),
        migrations.AddField(
            model_name='additionalpage',
            name='content_en',
            field=models.TextField(null=True, verbose_name='Sisu'),
        ),
        migrations.AddField(
            model_name='additionalpage',
            name='content_et',
            field=models.TextField(null=True, verbose_name='Sisu'),
        ),
        migrations.AddField(
            model_name='additionalpage',
            name='title_en',
            field=models.CharField(null=True, verbose_name='Pealkiri', max_length=255),
        ),
        migrations.AddField(
            model_name='additionalpage',
            name='title_et',
            field=models.CharField(null=True, verbose_name='Pealkiri', max_length=255),
        ),
        migrations.AddField(
            model_name='carouselslide',
            name='content_en',
            field=models.TextField(verbose_name='Sisu', help_text="Sisu kasutatakse kui HTMLi, seega võib kasutada linke: (<a class='...' href='...' target='_blank'>Link</a>) jne.", null=True),
        ),
        migrations.AddField(
            model_name='carouselslide',
            name='content_et',
            field=models.TextField(verbose_name='Sisu', help_text="Sisu kasutatakse kui HTMLi, seega võib kasutada linke: (<a class='...' href='...' target='_blank'>Link</a>) jne.", null=True),
        ),
        migrations.AddField(
            model_name='carouselslide',
            name='link_text_en',
            field=models.CharField(null=True, verbose_name='Nupu tekst', max_length=50),
        ),
        migrations.AddField(
            model_name='carouselslide',
            name='link_text_et',
            field=models.CharField(null=True, verbose_name='Nupu tekst', max_length=50),
        ),
        migrations.AddField(
            model_name='carouselslide',
            name='title_en',
            field=models.CharField(null=True, verbose_name='Pealkiri', max_length=255),
        ),
        migrations.AddField(
            model_name='carouselslide',
            name='title_et',
            field=models.CharField(null=True, verbose_name='Pealkiri', max_length=255),
        ),
        migrations.AddField(
            model_name='concert',
            name='location_en',
            field=models.CharField(null=True, verbose_name='Asukoht', max_length=255),
        ),
        migrations.AddField(
            model_name='concert',
            name='location_et',
            field=models.CharField(null=True, verbose_name='Asukoht', max_length=255),
        ),
        migrations.AddField(
            model_name='concert',
            name='name_en',
            field=models.CharField(null=True, verbose_name='Pealkiri', max_length=255),
        ),
        migrations.AddField(
            model_name='concert',
            name='name_et',
            field=models.CharField(null=True, verbose_name='Pealkiri', max_length=255),
        ),
        migrations.AddField(
            model_name='contacttextblock',
            name='content_en',
            field=models.TextField(null=True, verbose_name='Sisu'),
        ),
        migrations.AddField(
            model_name='contacttextblock',
            name='content_et',
            field=models.TextField(null=True, verbose_name='Sisu'),
        ),
        migrations.AddField(
            model_name='contacttextblock',
            name='title_en',
            field=models.CharField(null=True, verbose_name='Pealkiri', max_length=255),
        ),
        migrations.AddField(
            model_name='contacttextblock',
            name='title_et',
            field=models.CharField(null=True, verbose_name='Pealkiri', max_length=255),
        ),
        migrations.AddField(
            model_name='management',
            name='job_en',
            field=models.CharField(null=True, verbose_name='Amet', max_length=255),
        ),
        migrations.AddField(
            model_name='management',
            name='job_et',
            field=models.CharField(null=True, verbose_name='Amet', max_length=255),
        ),
        migrations.AddField(
            model_name='repertory',
            name='composer_en',
            field=models.CharField(null=True, verbose_name='Helilooja', max_length=255),
        ),
        migrations.AddField(
            model_name='repertory',
            name='composer_et',
            field=models.CharField(null=True, verbose_name='Helilooja', max_length=255),
        ),
        migrations.AddField(
            model_name='repertory',
            name='lyrics_en',
            field=models.CharField(blank=True, null=True, verbose_name='Sõnade autor', max_length=255),
        ),
        migrations.AddField(
            model_name='repertory',
            name='lyrics_et',
            field=models.CharField(blank=True, null=True, verbose_name='Sõnade autor', max_length=255),
        ),
        migrations.AddField(
            model_name='repertory',
            name='title_en',
            field=models.CharField(null=True, verbose_name='Pealkiri', max_length=255),
        ),
        migrations.AddField(
            model_name='repertory',
            name='title_et',
            field=models.CharField(null=True, verbose_name='Pealkiri', max_length=255),
        ),
    ]
