import django
from django.conf.urls import patterns, include, url

from django.contrib import admin
from mxblog.views import user, blog, site

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', site.index, name='home'),
    url(r'^register/', user.register, name='register'),
    url(r'^login/', user.login, name='login'),
    url(r'^blog/(?P<bid>\d+)/', blog.blog, name='blog'),
    url(r'^archive/', blog.archive, name='archive'),
    url(r'^about/', site.about, name='about'),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
