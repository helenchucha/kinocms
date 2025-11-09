from django import forms
from .models import HmPage, Pages

class HmPageForm(forms.ModelForm):
    class Meta:
        model = HmPage
        fields = ['title', 'description', 'top_banner', 'status']
        # додайте потрібні поля

class PagesForm(forms.ModelForm):
    class Meta:
        model = Pages
        fields = ['title', 'description', 'top_banner', 'status', 'is_default']
        # додайте потрібні поля

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
        elif model_type == 'page':
            self.Meta.model = Pages
            self.Meta.fields = [
                'title', 'description', 'top_banner', 'status', 'is_default'
            ]
        else:
            raise ValueError("Unknown model_type. Використовуйте 'hm_page' або 'page'.")