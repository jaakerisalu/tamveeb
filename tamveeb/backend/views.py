import datetime
from django.views.generic import TemplateView
from backend.models import Concert, CarouselSlide


class MusicView(TemplateView):
    template_name = 'muusika.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        now = datetime.datetime.now()

        context.update({
            'concerts': Concert.objects.filter(date__gte=now.date()),
        })
        return self.render_to_response(context)


class LandingView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        context.update({
            'slides': CarouselSlide.objects.all(),
        })

        print(context['slides'])
        return self.render_to_response(context)
