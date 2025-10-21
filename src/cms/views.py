from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from user.models import User
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from .user_edit_form import UserEditForm
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .cities import CITIES

# def dashboard(request):
#    return render(request, 'admin_base.html')

def admin_panel(request):
    return render(request, 'cms/admin_base.html')

def user_list(request):
    user_list = User.objects.all().order_by('id')
    paginator = Paginator(user_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'cms/users.html', {
        'page_obj': page_obj,
        'active_page': 'users',
        'page_title': 'Пользователи',
    })

def user_edit(request, user_id):
    user_instance = get_object_or_404(User, id=user_id)
    sorted_cities = sorted(CITIES)

    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user_instance)
        if form.is_valid():
            form.save()
            messages.success(request, f'Користувач {user_instance.nickname} успішно оновлений.')
            return redirect('user_list')
        else:
            print("Помилка в формі:", form.errors)
    else:
        form = UserEditForm(instance=user_instance)

    return render(request, 'cms/user_edit.html', {
        'form': form,
        'user': user_instance,
        'active_page': 'users',
        'page_title': 'Редактировать пользователя',
        'cities': sorted_cities,
    })

User = get_user_model()

def check_nickname(request):
    nickname = request.GET.get('nickname', '').strip()
    print('Checking nickname:', nickname)
    exists = User.objects.filter(nickname=nickname).exists()
    print('Exists:', exists)
    return JsonResponse({'exists': exists})

def user_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.success(request, f'Пользователь {user.nickname} успешно удален.')
    # перехід назад до списку користувачів
    return redirect(f"{reverse('user_list')}?page={request.GET.get('page', '1')}")

def statistics(request):
    return render(request, 'cms/statistics.html', {
        'active_page': 'statistics',
        'page_title': 'Статистика',
    })

def banners(request):
    return render(request, 'cms/banners.html', {
        'active_page': 'banners',
        'page_title': 'Баннеры',
    })

def films(request):
    return render(request, 'cms/films.html', {
        'active_page': 'films',
        'page_title': 'Фильмы',
    })

def cinemas(request):
    return render(request, 'cms/cinemas.html', {
        'active_page': 'cinemas',
        'page_title': 'Кинотеатры',
    })

def news(request):
    return render(request, 'cms/news.html', {
        'active_page': 'news',
        'page_title': 'Новости',
    })

def shares(request):
    return render(request, 'cms/shares.html', {
        'active_page': 'shares',
        'page_title': 'Акции',
    })

def pages(request):
    return render(request, 'cms/pages.html', {
        'active_page': 'pages',
        'page_title': 'Страницы',
    })

def mailing(request):
    return render(request, 'cms/mailing.html', {
        'active_page': 'mailing',
        'page_title': 'Рассылка',
    })