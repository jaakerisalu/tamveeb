from django import forms
from django.contrib import admin
from backend.models import SeasonSponsor, CarouselSlide, Concert, Repertory, AboutUsTextBlock, Management, ContactUs, ContactTextBlock, AdditionalPage


class AdditionalPageForm(forms.ModelForm):
    def clean_visible(self):
        if self.cleaned_data["visible"] is True:  # If we try to set this one to True, hide the rest, if any
            AdditionalPage.objects.filter(visible=True).update(visible=False)
        return self.cleaned_data["visible"]


class AdditionalPageAdmin(admin.ModelAdmin):
    form = AdditionalPageForm


admin.site.register(SeasonSponsor)
admin.site.register(CarouselSlide)
admin.site.register(Concert)
admin.site.register(Repertory)
admin.site.register(AboutUsTextBlock)
admin.site.register(Management)
admin.site.register(ContactUs)
admin.site.register(ContactTextBlock)
admin.site.register(AdditionalPage, AdditionalPageAdmin)

