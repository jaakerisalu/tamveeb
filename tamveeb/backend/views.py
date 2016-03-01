import datetime
from django.views.generic import TemplateView
from backend.models import SeasonSponsor, CarouselSlide, Concert, Repertory, AboutUsTextBlock, Management, ContactUs, ContactTextBlock, AdditionalPage


class LandingView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        context.update({
            'additional_page': AdditionalPage.objects.all(),
            'slides': CarouselSlide.objects.all(),
             'season_sponsor': SeasonSponsor.objects.all(),
        })


        return self.render_to_response(context)

class MusicView(TemplateView):
    template_name = 'muusika.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        now = datetime.datetime.now()

        context.update({
            'additional_page': AdditionalPage.objects.all(),
            'concerts': Concert.objects.filter(date__gte=now.date()),
            'repertorys': Repertory.objects.all(),
            'season_sponsor': SeasonSponsor.objects.all(),
        })

        return self.render_to_response(context)

class AboutUsView(TemplateView):
    template_name = 'meist.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        context.update({
            'additional_page': AdditionalPage.objects.all(),
            'text_blocks': list(AboutUsTextBlock.objects.all()),  #QuerySet tehakse listiks, et template'is seda kasutada.
            'managements': Management.objects.all(),
            'season_sponsor': SeasonSponsor.objects.all(),
        })

        return self.render_to_response(context)

class ContactView(TemplateView):
    template_name = 'kontakt.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        context.update({
            'additional_page': AdditionalPage.objects.all(),
            'contact_us': ContactUs.objects.all(),
            'text_blocks': list(ContactTextBlock.objects.all()),
            'season_sponsor': SeasonSponsor.objects.all(),
        })

        return self.render_to_response(context)

class TemplateView(TemplateView):
    template_name = 'lisaleht.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        context.update({
            'additional_page': AdditionalPage.objects.all(),
            'season_sponsor': SeasonSponsor.objects.all(),
        })

        return self.render_to_response(context)
