from django.db import models
from .enums import STATUS_CHOICES

class HmPage(models.Model):
    title = models.CharField(max_length=255, default='Главная')
    description = models.TextField(blank=True, null=True)
    top_banner = models.ImageField(upload_to='main/', blank=True, null=True)
    phone1 = models.CharField(max_length=20, blank=True, null=True)
    phone2 = models.CharField(max_length=20, blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(choices=STATUS_CHOICES, default=True)

    # Поле для прив'язки до шаблону
    template_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Путь к шаблону, например: 'main/index.html'"
    )

    def __str__(self):
        return self.title

class Pages(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    top_banner = models.ImageField(upload_to='main/', blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(choices=STATUS_CHOICES, default=False)
    default = models.BooleanField(default=False)

    # Поле для прив'язки до шаблону
    template_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Путь к шаблону, например: 'main/index.html'"
    )

    def __str__(self):
        return self.title

class Seo(models.Model):
    url = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=255, blank=True)
    keywords = models.CharField(max_length=500, blank=True)
    description = models.TextField(blank=True)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.url

class Cinema(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    condition = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=225, null=True, blank=True)
    logo = models.ImageField(upload_to='main/', blank=True, null=True)
    top_banner = models.ImageField(upload_to='main/', blank=True, null=True)
    location = models.CharField(
        max_length=50,
        help_text='Укажите координаты в формате "ширина, долгота" (например: "50.1234, 30.5678")',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    def get_lat_lon(self):
        """Повертає ширину і довжину як кортеж (lat, lon), або None, якщо неправильно."""
        if self.location:
            try:
                lat_str, lon_str = self.location.split(',')
                return float(lat_str.strip()), float(lon_str.strip())
            except ValueError:
                return None
        return None
