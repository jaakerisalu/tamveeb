from functools import wraps
import os
import uuid
from django.db import models
from django.utils.decorators import available_attrs

# AIQ JA DAN, ÄRGE PANGE TÄHELE
# Teeb folderi, kuhu pildid uploaditakse
def random_path(instance, filename):
    """ Random path generator for uploads, specify this for upload_to= argument of FileFields
    """
    # Split the uuid into two parts so that we won't run into subdirectory count limits. First part has 3 hex chars,
    #  thus 4k possible values.
    uuid_hex = uuid.uuid4().hex
    return os.path.join(uuid_hex[:3], uuid_hex[3:], filename)

def path_prefix(prefix):
    def decorator(func):
        @wraps(func, assigned=available_attrs(func))
        def _wrapped_func(*args, **kwargs):
            return os.path.join(prefix, func(*args, **kwargs))
        return _wrapped_func
    return decorator
# VÕITE JÄTKATA

@path_prefix('carousel')
def random_carousel_image_path(instance, filename):
    return random_path(instance, filename)

@path_prefix('about_us')
def random_about_us_image_path(instance, filename):
    return random_path(instance, filename)

class Concert(models.Model):
    date = models.DateField('Kuupäev')
    time = models.TimeField('Kellaaeg')
    name = models.CharField('Pealkiri', max_length=255)
    location = models.CharField('Asukoht', max_length=255)
    ticket_sales_site = models.URLField('Piletimüügi leht', blank=True, null=True)

    def __str__(self):
        return self.name + " " + self.location


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
    content = models.TextField('Sisu', help_text="Sisu kasutatakse kui HTML-i, võid kasutada linke: (<a class='yyy' href='xxx' target='_blank'>Link</a>) jne")
    link_text = models.CharField('Nupu tekst', max_length=50)
    link = models.CharField('Nupu link', choices=LINK_CHOICES, help_text='Mis lehele meie saidil antud slaid viitab', max_length=20)
    anchor = models.CharField('Nupu lingi ankur', max_length=255, help_text='Kui tahad et link viiks mõne lehel asuva ankru juurde, siis kirjuta see siia', blank=True, null=True)
    image = models.ImageField('Pilt', upload_to=random_carousel_image_path)

    def __str__(self):
        return self.title


class AboutUsTextBlock(models.Model):
    LEFT = 'left'
    RIGHT = 'right'
    ALIGNMENT_CHOICES = (
        (LEFT, 'Vasakul'),
        (RIGHT, 'Paremal'),
    )

    alignment = models.CharField('Pildi asukoht', choices=ALIGNMENT_CHOICES, help_text='Kummal pool teksti asub pilt', max_length=20)
    title = models.CharField('Pealkiri', max_length=255)
    content = models.TextField('Sisu', help_text="Sisu")
    image = models.ImageField('Pilt', upload_to=random_about_us_image_path)

    order = models.SmallIntegerField('Järjekord', help_text='Väiksem = ülevalpool', default=0)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title
