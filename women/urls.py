from django.urls import path, re_path
from .views import *

urlpatterns = [
    # path('', index, name='home'),
    # path('category/<slug:category_slug>/', show_category, name='category'),
    path('', WomenHome.as_view(), name='home'),
    path('category/<slug:category_slug>/', ShowCategory.as_view(), name='category'),

    path('about', about, name='about'),
    path('feedback', feedback, name='feedback'),
    path('login', login, name='login'),
    # path('add_page', addpage, name='add_page'),
    path('add_page', AddPage.as_view(), name='add_page'),
    path('cats/<int:catId>/'
         '', categories),
    # path('post/<slug:post_slug>/', show_post, name='post'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]


