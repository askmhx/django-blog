import json
from django.db.models import F
from django.http import HttpResponse
from django.template.response import TemplateResponse
from mxblog.models import Blog, BlogGroup

__author__ = 'diaoer'


def blog(request, bid=0):
    blog = Blog.objects.get(id=bid)
    return TemplateResponse(request, 'blog.html', {"navloc": "blog", "blog": blog})


def archive(request):
    bloglist = Blog.objects.all()
    return TemplateResponse(request, 'archive.html', {"navloc": "archive", "bloglist": bloglist})


def thumbs(request, ctype, bid):
    if ctype == 'support':
        Blog.objects.filter(id=bid).update(support=F('support') + 1)
    elif ctype == 'oppose':
        Blog.objects.filter(id=bid).update(oppose=F('oppose') + 1)

    dict = {'result': 'success'}
    return HttpResponse(json.dumps(dict), mimetype='application/json')

