from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from backend.views import MusicView, LandingView, AboutUsView, ContactView, TemplateView

admin.autodiscover()

urlpatterns = [
    url(r'', include('accounts.urls')),
    url(r'^tagauks/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n'))
]

urlpatterns += i18n_patterns(
    url(r'^$', LandingView.as_view(), name='home'),
    url(_(r'^muusika/$'), MusicView.as_view(), name='muusika'),
    url(_(r'^meist/$'), AboutUsView.as_view(), name='meist'),
    url(_(r'^kontakt/$'), ContactView.as_view(), name='kontakt'),
    url(_(r'^lisaleht/$'), TemplateView.as_view(template_name='lisaleht.html'), name='lisaleht')
)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
