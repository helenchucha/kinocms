from cms.models import HmPage, Pages


def format_phone(phone):
    digits = ''.join(filter(str.isdigit, phone))
    if len(digits) == 11:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:8]}-{digits[8:]}"
    elif len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:8]}-{digits[8:]}"
    else:
        return phone


def phones(request):
    hmpage = HmPage.objects.first()
    phone1 = hmpage.phone1 if hmpage else ''
    phone2 = hmpage.phone2 if hmpage else ''

    # Отримуємо меню: тільки ті записи, де is_default=True
    # menu_items = Pages.objects.filter(is_default=True)

    menu_items = [
        {
            'name': page.title,
            'url_name': 'page_detail',
            'slug': page.slug,
            'children': [],  # якщо є підменю
        }
        for page in Pages.objects.all()
    ]
    print(menu_items)

    return {
        'phone1': format_phone(phone1),
        'phone2': format_phone(phone2),
        'menu_items': menu_items,
    }
