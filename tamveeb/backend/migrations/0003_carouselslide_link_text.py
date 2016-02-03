# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_carouselslide'),
    ]

    operations = [
        migrations.AddField(
            model_name='carouselslide',
            name='link_text',
            field=models.CharField(verbose_name='Nupu tekst', default='Vajuta siia', max_length=50),
            preserve_default=False,
        ),
    ]
