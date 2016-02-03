from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import TemplateView
from backend.views import MusicView, LandingView, AboutUsView

admin.autodiscover()

urlpatterns = [
    url(r'', include('accounts.urls')),
    url(r'^$', LandingView.as_view(), name='home'),
    url(r'^muusika/$', MusicView.as_view(), name='muusika'),
    url(r'^meist/$', AboutUsView.as_view(), name='meist'),
    url(r'^kontakt/$', TemplateView.as_view(template_name='kontakt.html'), name='kontakt'),
    url(r'^lisaleht/$', TemplateView.as_view(template_name='lisaleht.html'), name='lisaleht'),

    url(r'^tagauks/', include(admin.site.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
