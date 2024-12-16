from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name='start'),  # Главная страница
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('profile', views.profile, name='profile'),
    path('main', views.main, name='main'),
    path('catalog', views.catalog, name='catalog'),
    path('detail', views.detail, name='detail'),
    path('filtr', views.filtr, name='filtr'),
    path('search', views.search, name='search'),
    path('recommendation', views.recommendation, name='recommendation'),
    path('myexc', views.myexc, name='myexc'),
    path('favorits', views.favorits, name='favorits'),

]