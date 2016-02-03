from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import TemplateView


admin.autodiscover()

urlpatterns = [
    url(r'', include('accounts.urls')),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^muusika/$', TemplateView.as_view(template_name='muusika.html'), name='muusika'),
    url(r'^meist/$', TemplateView.as_view(template_name='meist.html'), name='meist'),
    url(r'^kontakt/$', TemplateView.as_view(template_name='kontakt.html'), name='kontakt'),
    url(r'^topelttuur/$', TemplateView.as_view(template_name='topelttuur.html'), name='topelttuur'),

    url(r'^tagauks/', include(admin.site.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
