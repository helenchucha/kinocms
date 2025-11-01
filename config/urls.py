from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = ([
    path('', include('main.urls')),
    path('', include('authentication.urls')),
    path('admin/', include('cms.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('cms.urls')),
    path('user/', include('user.urls')),
    # path('login/', auth_views.LoginView.as_view(template_name='cms/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
               # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))