from modeltranslation.translator import register, TranslationOptions
from .models import HmPage, Seo

@register(HmPage)
class HmPageTranslationOptions(TranslationOptions):
    fields = ('title','description',)

@register(Seo)
class SeoTranslationOptions(TranslationOptions):
    fields = ('seo_title','seo_description', 'seo_text',)