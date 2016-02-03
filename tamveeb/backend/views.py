import datetime
from django.views.generic import TemplateView
from backend.models import Concert, CarouselSlide, AboutUsTextBlock


class MusicView(TemplateView):
    template_name = 'muusika.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        now = datetime.datetime.now()

        context.update({
            'concerts': Concert.objects.filter(date__gte=now.date()),
            #'songs': Song.objects.all()
        })
        return self.render_to_response(context)


class LandingView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        context.update({
            'slides': CarouselSlide.objects.all(),
        })

        return self.render_to_response(context)


class AboutUsView(TemplateView):
    template_name = 'meist.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        context.update({
            'text_blocks': list(AboutUsTextBlock.objects.all()),  # Ma teen siin QuerySeti listiks, et templates VIIMAST saaks küsida
        })

        return self.render_to_response(context)
