from cms.models import HmPage, Pages, Seo


def format_phone(phone):
    digits = ''.join(filter(str.isdigit, phone))
    if len(digits) == 11:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:8]}-{digits[8:]}"
    elif len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:8]}-{digits[8:]}"
    else:
        return phone


def main_page(request):
    # Отримати всі сторінки
    pages = Pages.objects.all()

    # Вибрати головні пункти меню (без підменю)
    main_menu_pages = pages.filter(is_default=True, is_child=False)

    # Сторінка, яка має підменю (О кинотеатре)
    parent_page_slug = 'o-kinoteatre'
    parent_page = pages.filter(slug=parent_page_slug).first()

    hmpage = HmPage.objects.first()
    status = hmpage.status
    phone1 = hmpage.phone1 if hmpage else ''
    phone2 = hmpage.phone2 if hmpage else ''

    # Отримуємо меню: тільки ті записи, де is_default=True
    # menu_items = Pages.objects.filter(is_default=True)

    # menu_items = [
    #     {
    #         'name': page.title,
    #         'url_name': 'page_detail',
    #         'slug': page.slug,
    #         'children': [],  # якщо є підменю
    #     }
    #     for page in Pages.objects.all()
    # ]
    # print(menu_items)

    menu_items = []
    for page in main_menu_pages:
        children = []
        if page == parent_page:
            # Для "О кинотеатре" виводимо всі сторінки з is_child=True
            children = pages.filter(is_child=True)
        menu_items.append({
            'name': page.title,
            'url_name': 'page_detail',
            'slug': page.slug,
            'children': [
                {
                    'title': child.title,
                    'url_name': 'page_detail',
                    'slug': child.slug
                } for child in children
            ],
        })

    return {
        'status': status,
        'phone1': format_phone(phone1),
        'phone2': format_phone(phone2),
        'menu_items': menu_items,
    }

def main_page_seo(request):
    hmpage_instance = HmPage.objects.get(id=1)
    seo_data = Seo.objects.filter(page=hmpage_instance).first()
    return {
        'seo': seo_data
    }