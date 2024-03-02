from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render, get_object_or_404
from women.models import *
from women.forms import *


# Create your views here.


#
# def index(request):
#     return HttpResponse(f"Отображение статьи")
#
def index(request):
    posts = Women.objects.all()
    context = {'posts': posts, 'title': "Главная страница", 'cat_selected': 0}
    return render(request, 'women/index.html/', context)


def about(request):
    return render(request, 'women/about.html/', {'title': "О сайте"})


def feedback(request):
    return render(request, 'women/feedback.html/', {'title': "Обратная связь"})


def login(request):
    return render(request, 'women/login.html/', {'title': "Авторизация"})


# форма, не связанная с моделью
# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST)
#         if form.is_valid():
#             try:
#                 Women.objects.create(**form.cleaned_data)
#                 return redirect('home')  # Добавлен явный возврат
#             except Exception as e:
#                 form.add_error(None, f'Ошибка добавления поста: {str(e)}')  # Исправлено добавление ошибки
#     else:
#         form = AddPostForm()
#     return render(request, 'women/addPage.html/', {'form': form, 'title': "Добавить статью"})


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)

        # print(form.is_valid())

        if form.is_valid():
            form.save()
            return redirect('home')  # Добавлен явный возврат
        else:
            # Получаем словарь ошибок из формы
            errors = form.errors
            print(errors)  # Выводим ошибки в консоль для отладки
    else:
        form = AddPostForm()
    return render(request, 'women/addPage.html/', {'form': form, 'title': "Добавить статью"})


def show_category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    posts = Women.objects.all().filter(cat_id=category.pk)
    if len(posts) == 0:
        raise Http404()
    context = {'cat_selected': category.pk, 'posts': posts, 'title': "Отображение по рубрикам"}
    return render(request, 'women/index.html/', context)


# def show_post(request, post_id):
#     posts = Women.objects.all()
#     return render(request, 'women/post.html/', {'post': posts[post_id].content})

def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    cat_selected = post.cat_id
    return render(request, 'women/post.html', {'post': post, 'cat_selected': cat_selected})


# def show_post(request, post_id):
#     return HttpResponse(f"Отображение статьи с id = {post_id}")

def categories(request, catId):
    if (request.GET): print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catId}</p>")


def archive(request, year):
    if int(year) > 2020:
        # raise Http404()
        # return redirect('/')
        return redirect('home', permanent=True)

    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1")
