from django.template.response import TemplateResponse

from mxblog.models import Post

__author__ = 'MengHX'


def index(request):
    bloglist = Post.objects.all()[:6]
    return TemplateResponse(request, 'index.html', {"bloglist": bloglist})


def about(request):
    return TemplateResponse(request, 'about.html', {})


def start(request):
    return TemplateResponse(request, 'start.html', {})


def tags(request):
    return TemplateResponse(request, 'index.html')
