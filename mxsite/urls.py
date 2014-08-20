from django.conf.urls import patterns, include, url
from django.contrib import admin

from mxblog.views import user, post, site
from mxblog.views.start import StartView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', site.index, name='home'),
    url(r'^register/', user.register, name='register'),
    url(r'^login/', user.login, name='login'),
    url(r'^post/(?P<bid>\d+)/', post.blog, name='post'),
    url(r'^thumbs/(?P<ctype>(support)|(oppose))/(?P<bid>\d+)/', post.thumbs),
    url(r'^archive/', post.archive, name='archive'),
    url(r'^start/', StartView.as_view(), name='start'),
    url(r'^about/', site.about, name='about'),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
