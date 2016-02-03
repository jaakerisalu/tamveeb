# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_aboutustextblock'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutustextblock',
            options={'ordering': ['order', 'title']},
        ),
        migrations.AddField(
            model_name='aboutustextblock',
            name='order',
            field=models.SmallIntegerField(default=0, verbose_name='Järjekord', help_text='Väiksem = ülevalpool'),
        ),
    ]
