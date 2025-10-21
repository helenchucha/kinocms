from django.shortcuts import render

def get_menu():
    return [
        {'name': 'Афиша', 'url_name': '', 'children': [], },
        {'name': 'Расписание', 'url_name': '', 'children': [], },
        {'name': 'Скоро', 'url_name': '', 'children': [], },
        {'name': 'Кинотеатры', 'url_name': '', 'children': [], },
        {'name': 'Акции', 'url_name': '', 'children': [], },
        {
            'name': 'О кинотеатре',
            'url_name': 'about',
            'children': [
                 {'name': 'Новости', 'url_name': ''},
                 {'name': 'Реклама', 'url_name': ''},
                 {'name': 'Кафе', 'url_name': ''},
                 {'name': 'Мобильные приложения', 'url_name': ''},
                 {'name': 'Контакты', 'url_name': ''},
                ],
        },
    ]

def index(request):
    menu_items = get_menu()
    print(menu_items)
    return render(request, 'main/index.html', {'menu_items': menu_items})

def about(request):
    menu_items = get_menu()
    print(menu_items)
    return render(request, 'main/about.html', {'menu_items': menu_items})