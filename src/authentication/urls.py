from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='cms/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('register/', views.register_view, name='register'),
]