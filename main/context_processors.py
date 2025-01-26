def menu_and_authenticate(request):
    return {
        'menu': [
            {'title': 'About', 'url_name': 'about'},
            {'title': 'Contact', 'url_name': 'contact'},
            {'title': 'Pricing', 'url_name': 'pricing'},
            {'title': 'Resources', 'url_name': 'resources'}
        ],
        'authenticate': [
            {'title': 'Login', 'url_name': 'accounts:login'},
            {'title': 'Register', 'url_name': 'accounts:register'},
        ],
    }