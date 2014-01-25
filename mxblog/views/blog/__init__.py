from django.template.response import TemplateResponse
from mxblog.models import Blog, BlogGroup

__author__ = 'diaoer'


def blog(request, bid=0):
    blog = Blog.objects.get(id=bid)
    return TemplateResponse(request, 'blog.html', {"navloc": "blog", "blog": blog})


def archive(request):
    bloglist = Blog.objects.all()
    return TemplateResponse(request, 'archive.html', {"navloc": "archive", "bloglist": bloglist})
