from django.shortcuts import render, redirect
from django.http import HttpResponse

def start(request):
    return render(request, 'start.html')

def register(request):
    """Регистрация пользователя"""
    if request.method == 'POST':
        name = request.POST.get('name')  # Получаем имя пользователя
        email = request.POST.get('email')  # Получаем почту пользователя
        password = request.POST.get('password')  # Получаем пароль пользователя

        # Сохраняем данные в сессии
        request.session['user_name'] = name
        request.session['user_email'] = email
        request.session['user_password'] = password

        return redirect('login')  # Перенаправляем на страницу входа
    return render(request, 'register.html')

def login(request):
    """Вход пользователя"""
    if request.method == 'POST':
        email = request.POST.get('email')  # Получаем введённую почту
        password = request.POST.get('password')  # Получаем введённый пароль

        # Проверка данных пользователя из сессии
        saved_email = request.session.get('user_email')
        saved_password = request.session.get('user_password')

        if email == saved_email and password == saved_password:
            return redirect('main')  # Перенаправляем в личный кабинет
        else:
            return HttpResponse("Неверные данные! Попробуйте снова.")

    return render(request, 'login.html')


def profile(request):
    """Личный кабинет пользователя"""
    name = request.session.get('user_name', 'Гость')  # Получаем имя пользователя из сессии
    return render(request, 'profile.html', {'name': name})


def main(request):
    return render(request, 'main.html')


def catalog(request):
    return render(request, 'catalog.html')


def detail(request):
    return render(request, 'detail.html')


def filtr(request):
    return render(request, 'filtr.html')


def search(request):
    return render(request, 'search.html')


def recommendation(request):
    return render(request, 'recommendation.html')

def myexc(request):
    return render(request, 'myexc.html')


def favorits(request):
    return render(request, 'favorits.html')
