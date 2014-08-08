from django.template.response import TemplateResponse
from mxblog.models import Blog

__author__ = 'diaoer'


def index(request):
    bloglist = Blog.objects.all()[:6]
    return TemplateResponse(request, 'index.html', {"navloc": "home", "bloglist": bloglist})

def about(request):
    return TemplateResponse(request, 'about.html', {"navloc": "about"})


def start(request):
    return TemplateResponse(request, 'start.html', {"navloc": "start"})

def tags(request):
    return TemplateResponse(request, 'index.html')
