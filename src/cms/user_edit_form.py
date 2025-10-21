from django import forms
from user.models import User
from django.core.exceptions import ValidationError
import re
from src.user.enums import GENDER_CHOICES, LANGUAGE_CHOICES

# Валідатор для номера телефону
def validate_phone(value):
    pattern = re.compile(r'^\+\d{11,15}$')  # формат +код_країни і номер
    if not pattern.match(value):
        raise ValidationError('Enter a valid phone number (e.g. +12125552368).')

class UserEditForm(forms.ModelForm):
    email = forms.EmailField(required=False)
    phone = forms.CharField(required=False, validators=[validate_phone])
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect, required=False)
    language = forms.ChoiceField(choices=LANGUAGE_CHOICES, widget=forms.RadioSelect, required=False)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'gender', 'birth_date', 'nickname', 'address', 'phone', 'card',
                  'city', 'language']