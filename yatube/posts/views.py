# posts/views.py
from django.shortcuts import render


# Главная страница
def index(request):
    template = 'posts/index.html'
    title = 'Главная страница'
    context = {
        'title': title,
        'text': 'Это главная страница проекта Yatube'
    }
    return render(request, template, context)


# Страница с информацией о группе;
# view-функция принимает параметр slug:slug из path()
def group_posts(request, pk):
    template = 'posts/group_posts.html'
    title = 'slug:slug'
    context = {
        'title': title,
        'text': 'Список гроупс быть тут должен'
    }
    return render(request, template, context)
