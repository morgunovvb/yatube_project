# posts/views.py
from django.http import HttpResponse
# Импортируем загрузчик.
from django.template import loader
# Импортируем рендеринг
from django.shortcuts import render


# Главная страница
def index(request):
    template = 'posts/index.html'
    return render(request, template)

# Страница со списком групп
def groups(request):
    template = 'posts/groups.html'
    return render(request, template)

# Страница с информацией о группе;
# view-функция принимает параметр slug:slug из path()
def group_posts(request, pk):
    template = 'posts/group_posts.html'
    return render(request, template)

# Страница четвертая
def group_list(request):
    template = 'posts/group_list.html'
    return render(request, template)