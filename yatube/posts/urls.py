# posts/urls.py
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница постов
    path('groups/', views.groups),
    # Отдельная страница с информацией о посте
    path('group_posts/<slug:pk>/', views.group_posts),
    # Четвертая страница
    path('group_list.html/', views.group_list),
]