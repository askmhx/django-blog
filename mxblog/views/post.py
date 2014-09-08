import json

from django.db.models import F
from django.http import HttpResponse
from django.template.response import TemplateResponse
from mxblog.models import Post


__author__ = 'MengHX'


def post(request, bid=0):
    post = Post.objects.get(id=bid)
    return TemplateResponse(request, 'post.html', {"post": post})


def archive(request):
    postList = Post.objects.all()
    return TemplateResponse(request, 'archive.html', {"postList": postList})


def thumbs(request, ctype, bid):
    if ctype == 'support':
        Post.objects.filter(id=bid).update(support=F('support') + 1)
    elif ctype == 'oppose':
        Post.objects.filter(id=bid).update(oppose=F('oppose') + 1)

    dict = {'result': 'success'}
    return HttpResponse(json.dumps(dict), mimetype='application/json')

