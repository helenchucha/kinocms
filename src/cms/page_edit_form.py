from django import forms
from .models import HmPage, Pages, Seo

class HmPageForm(forms.ModelForm):
    class Meta:
        model = HmPage
        fields = ['title', 'description', 'top_banner', 'status', 'phone1', 'phone2']

class PagesForm(forms.ModelForm):
    class Meta:
        model = Pages
        fields = ['title', 'description', 'top_banner', 'status', 'is_default']

class SeoForm(forms.ModelForm):
    class Meta:
        model = Seo
        fields = ['seo_url', 'seo_title', 'seo_keywords', 'seo_description', 'seo_text']

class PageEditForm(forms.ModelForm):
    class Meta:
        model = None  # Тут залежить від того, яку модель ви хочете редагувати
        fields = []

    def __init__(self, *args, **kwargs):
        model_type = kwargs.pop('model_type', None)
        super().__init__(*args, **kwargs)
        if model_type == 'hm_page':
            self.Meta.model = HmPage
            self.Meta.fields = [
                'title', 'description', 'top_banner', 'phone1', 'phone2',
                'status'
            ]
            # додати поля seo
            self.fields['url'] = forms.CharField(max_length=200, required=False)
            self.fields['title'] = forms.CharField(max_length=255, required=False)
            self.fields['keywords'] = forms.CharField(max_length=500, required=False)
            self.fields['description'] = forms.CharField(widget=forms.Textarea, required=False)
            self.fields['text'] = forms.CharField(widget=forms.Textarea, required=False)
        elif model_type == 'page':
            self.Meta.model = Pages
            self.Meta.fields = [
                'title', 'description', 'top_banner', 'status', 'is_default'
            ]
            # додати поля seo
            self.fields['url'] = forms.CharField(max_length=200, required=False)
            self.fields['title'] = forms.CharField(max_length=255, required=False)
            self.fields['keywords'] = forms.CharField(max_length=500, required=False)
            self.fields['description'] = forms.CharField(widget=forms.Textarea, required=False)
            self.fields['text'] = forms.CharField(widget=forms.Textarea, required=False)
        else:
            raise ValueError("Unknown model_type. Використовуйте 'hm_page' або 'page'.")