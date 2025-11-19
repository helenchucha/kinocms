from django.apps import AppConfig


class AdminlteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cms'


class CmsConfig(AppConfig):
    name = 'src.cms'

    def ready(self):
        import src.cms.translation  # імпортуємо реєстрацію