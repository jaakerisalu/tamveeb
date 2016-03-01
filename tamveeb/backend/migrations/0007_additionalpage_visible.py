# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20160301_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='additionalpage',
            name='visible',
            field=models.BooleanField(default=False),
        ),
    ]
