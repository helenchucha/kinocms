from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.admin_panel, name='admin_panel'),  # тут викликається `admin_panel`, вже захищена декоратором
    path('admin/', views.admin_panel, name='admin_panel'),
    path('users/', views.user_list, name='user_list'),
    path('users/<int:user_id>/edit/', views.user_edit, name='user_edit'),
    path('users/<int:user_id>/delete/', views.user_delete, name='user_delete'),
    path('ajax/check-nickname/', views.check_nickname, name='check_nickname'),
    # path('page/<slug:slug>/', views.page_detail, name='page_detail'),
    path('stat/', views.statistics, name='statistics'),
    path('banners/', views.banners, name='banners'),
    path('films/', views.films, name='films'),
    path('cinemas/', views.cinemas, name='cinemas'),
    path('news/', views.news, name='news'),
    path('shares/', views.shares, name='shares'),
    path('pages/', views.page_list, name='page_list'),
    path('pages/edit/<int:page_id>/', views.page_edit, name='page_edit'),
    path('mailing/', views.mailing, name='mailing'),
]

# path('', views.dashboard, name='dashboard'),
# path('admin/', views.admin_redirect, name='admin_redirect'),
# path('admin/login/', views.admin_login, name='admin_login'),
