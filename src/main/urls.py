from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>', views.page_detail, name='page_detail'),
    path('about', views.about, name='about'),
    path('affiche', views.affiche, name='affiche'),
]
