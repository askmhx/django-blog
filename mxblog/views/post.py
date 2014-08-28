import json

from django.db.models import F
from django.http import HttpResponse
from django.template.response import TemplateResponse
from mxblog.models import Post


__author__ = 'MengHX'


def blog(request, bid=0):
    blog = Post.objects.get(id=bid)
    return TemplateResponse(request, 'blog.html', {"navloc": "blog", "blog": blog})


def archive(request):
    bloglist = Post.objects.all()
    return TemplateResponse(request, 'archive.html', {"navloc": "archive", "bloglist": bloglist})


def thumbs(request, ctype, bid):
    if ctype == 'support':
        Post.objects.filter(id=bid).update(support=F('support') + 1)
    elif ctype == 'oppose':
        Post.objects.filter(id=bid).update(oppose=F('oppose') + 1)

    dict = {'result': 'success'}
    return HttpResponse(json.dumps(dict), mimetype='application/json')

