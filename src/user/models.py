from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from .managers import UserManager
import secured_fields
from phonenumber_field.modelfields import PhoneNumberField
from .enums import GENDER_CHOICES, GENDER_MALE, GENDER_FEMALE, LANGUAGE_CHOICES, LANGUAGE_RU, LANGUAGE_UK

class User(AbstractUser):
    username = None  # Забороняємо використання username
    email = models.EmailField(unique=True)

    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        null=True,
        blank=True,
        default=GENDER_MALE
    )

    birth_date = models.DateField(null=True, blank=True)
    nickname = models.CharField(max_length=225)
    address = models.CharField(max_length=225, null=True, blank=True)
    phone = PhoneNumberField(null=True, blank=True, unique=True)
    card = secured_fields.EncryptedCharField(max_length=18, searchable=True, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    # role = models.CharField(max_length=10, choices=[('user', 'User'), ('admin', 'Admin')], default='user')

    language = models.CharField(
        max_length=2,
        choices=LANGUAGE_CHOICES,
        null=True,
        blank=True,
        default=LANGUAGE_RU
    )

    registration_date = models.DateTimeField(auto_now_add=True)  # Дата реєстрації

    # Для збереження паролів використовуйте set_password() та check_password().

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.nickname})"