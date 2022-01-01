# posts/urls.py
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # Страница постов
    path('group_posts/<slug:pk>/', views.group_posts, name='group_list')
]
