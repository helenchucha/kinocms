from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

handler403 = 'src.authentication.views.custom_permission_denied_view'

urlpatterns = ([
    path('', include('main.urls')),
    path('', include('authentication.urls')),
    path('admin/', include('cms.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('cms.urls')),
    path('user/', include('user.urls')),
    path('cms/', include('cms.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
               # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))