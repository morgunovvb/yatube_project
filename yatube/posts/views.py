# ice_cream/views.py
from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Главная страница')


# Страница со списком групп
def groups(request):
    return HttpResponse('Список групп')


# Страница с информацией о группе;
# view-функция принимает параметр slug:slug из path()
def group_posts(request, pk):
    return HttpResponse(f'Группа номер {pk}')