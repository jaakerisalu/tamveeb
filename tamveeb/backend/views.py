import datetime
from django.utils.translation import activate, get_language
from django.views.generic import TemplateView
from backend.models import SeasonSponsor, CarouselSlide, Concert, Repertory, AboutUsTextBlock, Management, ContactUs, ContactTextBlock, AdditionalPage

def merge_navbar_context(context):
    """
        Merges database objects used in the BaseTemplate into every view
    """
    additional_page = None
    if AdditionalPage.objects.filter(visible=True).count():
        additional_page = AdditionalPage.objects.filter(visible=True).first()

    context.update({
        'additional_page': additional_page,
        'season_sponsor': SeasonSponsor.objects.all(),
        'about_us_text_blocks': list(AboutUsTextBlock.objects.all()),  #QuerySet tehakse listiks, et template'is seda kasutada.
        'contact_text_blocks': list(ContactTextBlock.objects.all()),
    })
    return context


class LandingView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        context = merge_navbar_context(self.get_context_data(**kwargs))
        print(get_language())

        context.update({
            'slides': CarouselSlide.objects.all(),
        })

        return self.render_to_response(context)


class MusicView(TemplateView):
    template_name = 'muusika.html'

    def get(self, request, *args, **kwargs):
        context = merge_navbar_context(self.get_context_data(**kwargs))

        now = datetime.datetime.now()

        context.update({
            'concerts': Concert.objects.filter(date__gte=now.date()),
            'repertorys': Repertory.objects.all(),
        })

        return self.render_to_response(context)


class AboutUsView(TemplateView):
    template_name = 'meist.html'

    def get(self, request, *args, **kwargs):
        context = merge_navbar_context(self.get_context_data(**kwargs))

        context.update({
            'managements': Management.objects.all(),
        })

        return self.render_to_response(context)


class ContactView(TemplateView):
    template_name = 'kontakt.html'

    def get(self, request, *args, **kwargs):
        context = merge_navbar_context(self.get_context_data(**kwargs))

        context.update({
            'contact_us': ContactUs.objects.all(),
        })

        return self.render_to_response(context)


class TemplateView(TemplateView):
    template_name = 'lisaleht.html'

    def get(self, request, *args, **kwargs):
        context = merge_navbar_context(self.get_context_data(**kwargs))

        return self.render_to_response(context)
