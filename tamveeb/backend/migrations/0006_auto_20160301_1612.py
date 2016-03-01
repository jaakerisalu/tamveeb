# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import backend.models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20160203_1909'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalPage',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('image', models.ImageField(verbose_name='Pilt', upload_to=backend.models.random_additional_page_image_path)),
                ('title', models.CharField(max_length=255, verbose_name='Pealkiri')),
                ('content', models.TextField(verbose_name='Sisu')),
            ],
        ),
        migrations.CreateModel(
            name='ContactTextBlock',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('alignment', models.CharField(help_text='Pildi asukoht teksti suhtes.', verbose_name='Pildi asukoht', max_length=20, choices=[('left', 'Vasakul'), ('right', 'Paremal')])),
                ('title', models.CharField(max_length=255, verbose_name='Pealkiri')),
                ('content', models.TextField(verbose_name='Sisu')),
                ('image', models.ImageField(help_text='Eelistatav pildi resolutsioon on 500x500 pikslit. PNG laiendiga pildi saab mahult kokku pakkida aadressil: https://tinypng.com/.', verbose_name='Pilt', upload_to=backend.models.random_contact_image_path)),
                ('order', models.SmallIntegerField(default=0, help_text='Väiksema järjekorranumbriga tekst paikneb leheküljel üleval pool.', verbose_name='Järjekord')),
            ],
            options={
                'ordering': ['order', 'title'],
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('choir', models.CharField(max_length=255, verbose_name='Koor')),
                ('address', models.CharField(max_length=255, verbose_name='Aadress')),
                ('phone', models.CharField(max_length=255, verbose_name='Telefon')),
                ('email', models.CharField(max_length=255, verbose_name='E-post')),
                ('finance_email', models.CharField(help_text='Lepingud, arved jms.', verbose_name='Finants e-post', max_length=255)),
                ('homepage', models.URLField(verbose_name='Koduleht')),
                ('organization', models.CharField(max_length=255, verbose_name='Organisatsioon')),
                ('organization_address', models.CharField(max_length=255, verbose_name='Organisatsiooni aadress')),
                ('registry_number', models.IntegerField(verbose_name='Registri number')),
                ('vat', models.CharField(max_length=255, verbose_name='Käibemaksukohuslase number')),
            ],
        ),
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nimi')),
                ('job', models.CharField(max_length=255, verbose_name='Amet')),
                ('phone', models.CharField(max_length=255, blank=True, verbose_name='Telefon', null=True)),
                ('email', models.CharField(max_length=255, verbose_name='E-post')),
            ],
        ),
        migrations.CreateModel(
            name='Repertory',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Pealkiri')),
                ('composer', models.CharField(max_length=255, verbose_name='Helilooja')),
                ('lyrics', models.CharField(max_length=255, blank=True, verbose_name='Sõnade autor', null=True)),
                ('listen_site', models.URLField(help_text="Youtube'i embed-tüüpi link kujul: https://www.youtube.com/embed/...", verbose_name='Kuulamise leht')),
            ],
        ),
        migrations.CreateModel(
            name='SeasonSponsor',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('sponsor', models.CharField(max_length=255, verbose_name='Hooaja sponsor')),
            ],
        ),
        migrations.AlterField(
            model_name='aboutustextblock',
            name='alignment',
            field=models.CharField(help_text='Pildi asukoht teksti suhtes.', verbose_name='Pildi asukoht', max_length=20, choices=[('left', 'Vasakul'), ('right', 'Paremal')]),
        ),
        migrations.AlterField(
            model_name='aboutustextblock',
            name='content',
            field=models.TextField(verbose_name='Sisu'),
        ),
        migrations.AlterField(
            model_name='aboutustextblock',
            name='image',
            field=models.ImageField(help_text='Eelistatav pildi resolutsioon on 500x500 pikslit. PNG laiendiga pildi saab mahult kokku pakkida aadressil: https://tinypng.com/.', verbose_name='Pilt', upload_to=backend.models.random_about_us_image_path),
        ),
        migrations.AlterField(
            model_name='aboutustextblock',
            name='order',
            field=models.SmallIntegerField(default=0, help_text='Väiksema järjekorranumbriga tekst paikneb leheküljel üleval pool.', verbose_name='Järjekord'),
        ),
        migrations.AlterField(
            model_name='carouselslide',
            name='anchor',
            field=models.CharField(help_text='Ankur meie leheküljel, mille juurde link viib.', blank=True, verbose_name='Nupu lingi ankur', null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='carouselslide',
            name='content',
            field=models.TextField(help_text="Sisu kasutatakse kui HTMLi, seega võib kasutada linke: (<a class='...' href='...' target='_blank'>Link</a>) jne.", verbose_name='Sisu'),
        ),
        migrations.AlterField(
            model_name='carouselslide',
            name='link',
            field=models.CharField(help_text='Lehekülg meie saidil, millele antud slaid viitab.', verbose_name='Nupu link', max_length=20, choices=[('muusika', 'Muusika'), ('meist', 'Meist'), ('kontakt', 'Kontakt'), ('lisaleht', 'Lisaleht')]),
        ),
    ]
