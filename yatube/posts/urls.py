# posts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница постов
    path('groups/', views.posts),
    # Отдельная страница с информацией о посте
    path('groups/<slug:slug>/', views.group_posts),
]