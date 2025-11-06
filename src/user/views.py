from django.shortcuts import get_object_or_404, render, redirect
from user.models import User
from cms.user_edit_form import UserEditForm
from django.contrib import messages
from cms.cities import CITIES

# def profile_view(request):
#     return render(request, 'user/profile.html')

def profile_view(request):
    user_instance = request.user
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

    return render(request, 'user/profile.html', {
        'form': form,
        'user': user_instance,
        'active_page': 'users',
        'page_title': 'Кабинет пользователя',
        'cities': sorted_cities,
    })