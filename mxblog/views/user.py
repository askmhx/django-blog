from django.template.response import TemplateResponse

__author__ = 'MengHX'

def register(request):
    return TemplateResponse(request, 'register.html', {})


def login(request):
    return TemplateResponse(request, 'login.html', {})
