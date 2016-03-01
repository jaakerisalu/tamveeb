from functools import wraps
import os
import uuid

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.decorators import available_attrs

# Teeb folderi, kuhu pildid uploaditakse.
def random_path(instance, filename):
    """ Random path generator for uploads, specify this for upload_to= argument of FileFields.
    """
    # Split the uuid into two parts so that we won't run into subdirectory count limits. First part has 3 hex chars,
    # thus 4k possible values.
    uuid_hex = uuid.uuid4().hex
    return os.path.join(uuid_hex[:3], uuid_hex[3:], filename)

def path_prefix(prefix):
    def decorator(func):
        @wraps(func, assigned=available_attrs(func))
        def _wrapped_func(*args, **kwargs):
            return os.path.join(prefix, func(*args, **kwargs))
        return _wrapped_func
    return decorator

def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.id != model.objects.get().id):
        raise ValidationError("Objektist %s saab teha ainult ühe eksemplari!" % model.__name__)

@path_prefix('carousel')
def random_carousel_image_path(instance, filename):
    return random_path(instance, filename)

@path_prefix('about_us')
def random_about_us_image_path(instance, filename):
    return random_path(instance, filename)

@path_prefix('contact')
def random_contact_image_path(instance, filename):
    return random_path(instance, filename)

@path_prefix('additional_page')
def random_additional_page_image_path(instance, filename):
    return random_path(instance, filename)

class SeasonSponsor(models.Model):
    sponsor = models.CharField('Hooaja sponsor', max_length=255)

    def clean(self):
        validate_only_one_instance(self)

    def __str__(self):
        return self.sponsor

class CarouselSlide(models.Model):
    MUUSIKA = 'muusika'
    MEIST = 'meist'
    KONTAKT = 'kontakt'
    LISALEHT = 'lisaleht'
    LINK_CHOICES = (
        (MUUSIKA, 'Muusika'),
        (MEIST, 'Meist'),
        (KONTAKT, 'Kontakt'),
        (LISALEHT, 'Lisaleht'),
    )

    title = models.CharField('Pealkiri', max_length=255)
    content = models.TextField('Sisu', help_text="Sisu kasutatakse kui HTMLi, seega võib kasutada linke: (<a class='...' href='...' target='_blank'>Link</a>) jne.")
    link_text = models.CharField('Nupu tekst', max_length=50)
    link = models.CharField('Nupu link', choices=LINK_CHOICES, help_text='Lehekülg meie saidil, millele antud slaid viitab.', max_length=20)
    anchor = models.CharField('Nupu lingi ankur', max_length=255, help_text='Ankur meie leheküljel, mille juurde link viib.', blank=True, null=True)
    image = models.ImageField('Pilt', upload_to=random_carousel_image_path)

    def __str__(self):
        return self.title

class Concert(models.Model):
    date = models.DateField('Kuupäev')
    time = models.TimeField('Kellaaeg')
    name = models.CharField('Pealkiri', max_length=255)
    location = models.CharField('Asukoht', max_length=255)
    ticket_sales_site = models.URLField('Piletimüügi leht', blank=True, null=True)

    def __str__(self):
        return self.name + " " + self.location

class Repertory(models.Model):
    title = models.CharField('Pealkiri', max_length=255)
    composer = models.CharField('Helilooja', max_length=255)
    lyrics = models.CharField('Sõnade autor', max_length=255, blank=True, null=True)
    listen_site = models.URLField('Kuulamise leht', help_text="Youtube'i embed-tüüpi link kujul: https://www.youtube.com/embed/...")

    def __str__(self):
        return self.title

class AboutUsTextBlock(models.Model):
    LEFT = 'left'
    RIGHT = 'right'
    ALIGNMENT_CHOICES = (
        (LEFT, 'Vasakul'),
        (RIGHT, 'Paremal'),
    )

    alignment = models.CharField('Pildi asukoht', choices=ALIGNMENT_CHOICES, help_text='Pildi asukoht teksti suhtes.', max_length=20)
    title = models.CharField('Pealkiri', max_length=255)
    content = models.TextField('Sisu')
    image = models.ImageField('Pilt', help_text='Eelistatav pildi resolutsioon on 500x500 pikslit. PNG laiendiga pildi saab mahult kokku pakkida aadressil: https://tinypng.com/.', upload_to=random_about_us_image_path)

    order = models.SmallIntegerField('Järjekord', help_text='Väiksema järjekorranumbriga tekst paikneb leheküljel üleval pool.', default=0)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

class Management(models.Model):
    name = models.CharField('Nimi', max_length=255)
    job = models.CharField('Amet', max_length=255)
    phone = models.CharField('Telefon', max_length=255, blank=True, null=True)
    email = models.CharField('E-post', max_length=255)

    def __str__(self):
        return self.name

class ContactUs(models.Model):
    choir = models.CharField('Koor', max_length=255)
    address = models.CharField('Aadress', max_length=255)
    phone = models.CharField('Telefon', max_length=255)
    email = models.CharField('E-post', max_length=255)
    finance_email = models.CharField('Finants e-post', max_length=255, help_text='Lepingud, arved jms.')
    homepage = models.URLField('Koduleht')

    organization = models.CharField('Organisatsioon', max_length=255)
    organization_address = models.CharField('Organisatsiooni aadress', max_length=255)
    registry_number = models.IntegerField('Registri number')
    vat = models.CharField('Käibemaksukohuslase number', max_length=255)

    def clean(self):
        validate_only_one_instance(self)

    def __str__(self):
        return self.choir

class ContactTextBlock(models.Model):
    LEFT = 'left'
    RIGHT = 'right'
    ALIGNMENT_CHOICES = (
        (LEFT, 'Vasakul'),
        (RIGHT, 'Paremal'),
    )

    alignment = models.CharField('Pildi asukoht', choices=ALIGNMENT_CHOICES, help_text='Pildi asukoht teksti suhtes.', max_length=20)
    title = models.CharField('Pealkiri', max_length=255)
    content = models.TextField('Sisu')
    image = models.ImageField('Pilt', help_text='Eelistatav pildi resolutsioon on 500x500 pikslit. PNG laiendiga pildi saab mahult kokku pakkida aadressil: https://tinypng.com/.', upload_to=random_contact_image_path)

    order = models.SmallIntegerField('Järjekord', help_text='Väiksema järjekorranumbriga tekst paikneb leheküljel üleval pool.', default=0)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

class AdditionalPage(models.Model):

    image = models.ImageField('Pilt', upload_to=random_additional_page_image_path)
    title = models.CharField('Pealkiri', max_length=255)
    content = models.TextField('Sisu')

    def clean(self):
        validate_only_one_instance(self)

    def __str__(self):
        return self.title
