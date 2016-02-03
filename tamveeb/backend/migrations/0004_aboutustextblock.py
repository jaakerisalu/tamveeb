# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import backend.models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_carouselslide_link_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsTextBlock',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('alignment', models.CharField(choices=[('left', 'Vasakul'), ('right', 'Paremal')], max_length=20, verbose_name='Pildi asukoht', help_text='Kummal pool teksti asub pilt')),
                ('title', models.CharField(max_length=255, verbose_name='Pealkiri')),
                ('content', models.TextField(verbose_name='Sisu', help_text='Sisu')),
                ('image', models.ImageField(upload_to=backend.models.random_about_us_image_path, verbose_name='Pilt')),
            ],
        ),
    ]
