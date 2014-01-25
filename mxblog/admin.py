__author__ = 'MengHX'
from django.contrib import admin
from mxblog.models import Blog
from mxblog.models import BlogGroup
from mxblog.models import SiteConfig
from mxblog.models import User


class BlogAdmin(admin.ModelAdmin):
    fields = ('title', 'content', 'tags', 'group', 'author')
    list_display = ['title', 'author', 'create_time']


admin.site.register(Blog, BlogAdmin)


class BlogGroupAdmin(admin.ModelAdmin):
    fields = ['title', 'author']
    list_display = ['title', 'create_time']


admin.site.register(BlogGroup, BlogGroupAdmin)


class SiteConfigAdmin(admin.ModelAdmin):
    fields = ['info_key', 'info_value']
    list_display = ['info_key', 'info_value', 'create_time']


admin.site.register(SiteConfig, SiteConfigAdmin)


class UserAdmin(admin.ModelAdmin):
    fields = ('login_id', 'username', 'password', 'mobile', 'email', 'website')
    list_display = ['username', 'create_time']
    pass


admin.site.register(User, UserAdmin)