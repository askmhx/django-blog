from django.template.response import TemplateResponse

__author__ = 'diaoer'


def register(request):
    return TemplateResponse(request, 'register.html', {"navloc": "register"})


def login(request):
    return TemplateResponse(request, 'login.html', {"navloc": "login"})
