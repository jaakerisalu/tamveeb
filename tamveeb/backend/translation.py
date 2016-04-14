from modeltranslation.translator import translator, TranslationOptions
from backend.models import CarouselSlide, Concert, Repertory, AboutUsTextBlock, Management, ContactTextBlock, \
    AdditionalPage


class CarouselSlideTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'link_text')


class ConcertTranslationOptions(TranslationOptions):
    fields = ('name', 'location')


class RepertoryTranslationOptions(TranslationOptions):
    fields = ('composer', 'lyrics', 'title')


class AboutUsTextBlockTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

class ManagementTranslationOptions(TranslationOptions):
    fields = ('job',)


class ContactTextBlockTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


class AdditionalPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


translator.register(CarouselSlide, CarouselSlideTranslationOptions)
translator.register(Concert, ConcertTranslationOptions)
translator.register(Repertory, RepertoryTranslationOptions)
translator.register(AboutUsTextBlock, AboutUsTextBlockTranslationOptions)
translator.register(Management, ManagementTranslationOptions)
translator.register(ContactTextBlock, ContactTextBlockTranslationOptions)
translator.register(AdditionalPage, AdditionalPageTranslationOptions)
