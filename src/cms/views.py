from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404
from user.models import User
from cms.models import HmPage, Pages

from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from .user_edit_form import UserEditForm
from .page_edit_form import HmPageForm, PagesForm
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .cities import CITIES
from .decorators import staff_required


@staff_required
def admin_panel(request):
    return render(request, 'cms/admin_base.html')

@staff_required
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

def page_list(request):
    # Отримати головну сторінку (вона одна)
    main_page = HmPage.objects.first()

    # Формуємо словник для головної сторінки у форматі, схожому на pages_list
    main_page_info = {
        'type': 'main_page',
        'object': main_page,
        'title': main_page.title,
        'creation_date': main_page.creation_date,
        'status': 'ВКЛ' if main_page.status else 'ВИКЛ',
    }

    # Отримати всі інші сторінки
    other_pages_qs = Pages.objects.all()

    # Пагінація для інших сторінок
    paginator = Paginator(other_pages_qs, 10)  # 10 на сторінку
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Формуємо список для інших сторінок
    pages_list = []
    for page in page_obj.object_list:
        pages_list.append({
            'type': 'pages',
            'object': page,
            'title': page.title,
            'creation_date': page.creation_date,
            'status': 'ВКЛ' if page.status else 'ВИКЛ',
            'can_delete': not page.is_default,  # якщо default = True, то видаляти не можна
        })

    return render(request, 'cms/pages.html', {
        'main_page': main_page_info,
        'pages': pages_list,
        'page_obj': page_obj,
        'active_page': 'pages',
        'page_title': 'Страницы',
    })


def page_edit(request, page_id):
    # Спершу намагаємось знайти у HmPage
    try:
        page_instance = HmPage.objects.get(id=page_id)
        is_main_page = True
    except HmPage.DoesNotExist:
        # Якщо не знайдено, шукаємо у Pages
        page_instance = get_object_or_404(Pages, id=page_id)
        is_main_page = False

    # Вибираємо форму залежно від типу сторінки
    if is_main_page:
        PageEditForm = HmPageForm
        template_name = 'cms/hmpage_edit.html'
    else:
        PageEditForm = PagesForm
        template_name = 'cms/page_edit.html'

    if request.method == 'POST':
        form = PageEditForm(request.POST, instance=page_instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Страница успішно оновлена.')
            return redirect('page_list')  # переконайтеся, що цей URL існує
        else:
            print("Помилка у формі:", form.errors)
    else:
        form = PageEditForm(instance=page_instance)

    return render(request, template_name, {'form': form, 'page': page_instance})


def mailing(request):
    return render(request, 'cms/mailing.html', {
        'active_page': 'mailing',
        'page_title': 'Рассылка',
    })

# def page_detail(request, slug):
#     page = get_object_or_404(Pages, slug=slug)
#     context = {
#         'page': page,
#     }
#     return render(request, page.template_name, context)

# @staff_required_or_permission_denied
# def some_admin_only_view(request):
#     return render(request, 'admin_only.html')
