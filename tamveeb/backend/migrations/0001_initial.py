# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('date', models.DateField(verbose_name='Kuupäev')),
                ('time', models.TimeField(verbose_name='Kellaaeg')),
                ('name', models.CharField(verbose_name='Pealkiri', max_length=255)),
                ('location', models.CharField(verbose_name='Asukoht', max_length=255)),
                ('ticket_sales_site', models.URLField(null=True, blank=True, verbose_name='Piletimüügi leht')),
            ],
        ),
    ]
