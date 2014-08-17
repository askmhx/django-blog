from django.utils.decorators import method_decorator
from mxblog.forms import PostUserChangeForm, PostUserCreationForm

__author__ = 'MengHX'
from mxblog.models import Post, Comments, PostUser
from mxblog.models import PostMeta
from mxblog.models import PostMetaInfo
from mxblog.models import Links
from mxblog.models import LinkGroup
from mxblog.models import Config
from django.db import transaction
from django.conf import settings
from django.contrib import admin
from django.contrib.admin.options import IS_POPUP_VAR
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.utils.html import escape
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext, ugettext_lazy as _
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

csrf_protect_m = method_decorator(csrf_protect)
sensitive_post_parameters_m = method_decorator(sensitive_post_parameters())

class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'content', 'author')
    list_display = ['title', 'author', 'create_time']


class PostMetaAdmin(admin.ModelAdmin):
    fields = ['title', 'author', 'type']
    list_display = ['title', 'type', 'create_time']


class PostMetaInfoAdmin(admin.ModelAdmin):
    fields = ['post', 'meta']
    list_display = ['post', 'meta']


class CommentsAdmin(admin.ModelAdmin):
    fields = ['post', 'content', 'author']
    list_display = ['post', 'content', 'create_time']


class LinksAdmin(admin.ModelAdmin):
    fields = ['url', 'title']
    list_display = ['title', 'url', 'create_time']


class LinkGroupAdmin(admin.ModelAdmin):
    fields = ['title', 'author']
    list_display = ['title', 'create_time']


class ConfigAdmin(admin.ModelAdmin):
    fields = ('info_key', 'info_value')
    list_display = ['info_key', 'info_value', 'create_time']
    pass


class PostUserAdmin(admin.ModelAdmin):
    add_form_template = 'admin/auth/user/add_form.html'
    change_user_password_template = None
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('avatar', 'username', 'bio', 'mobile', 'site', 'birthday')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    form = PostUserChangeForm
    add_form = PostUserCreationForm
    change_password_form = AdminPasswordChangeForm
    list_display = ('email', 'username', 'is_staff', 'is_superuser', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'username', 'mobile', 'site')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super(PostUserAdmin, self).get_fieldsets(request, obj)

    def get_form(self, request, obj=None, **kwargs):
        defaults = {}
        if obj is None:
            defaults.update({
                'form': self.add_form,
                'fields': admin.util.flatten_fieldsets(self.add_fieldsets),
            })
        defaults.update(kwargs)
        return super(PostUserAdmin, self).get_form(request, obj, **defaults)

    def get_urls(self):
        from django.conf.urls import patterns
        return patterns('',
            (r'^(\d+)/password/$',
             self.admin_site.admin_view(self.user_change_password))
        ) + super(PostUserAdmin, self).get_urls()

    def lookup_allowed(self, lookup, value):
        if lookup.startswith('password'):
            return False
        return super(PostUserAdmin, self).lookup_allowed(lookup, value)

    @sensitive_post_parameters_m
    @csrf_protect_m
    @transaction.atomic
    def add_view(self, request, form_url='', extra_context=None):
        if not self.has_change_permission(request):
            if self.has_add_permission(request) and settings.DEBUG:
                raise Http404(
                    'Your user does not have the "Change user" permission. In '
                    'order to add users, Django requires that your user '
                    'account have both the "Add user" and "Change user" '
                    'permissions set.')
            raise PermissionDenied
        if extra_context is None:
            extra_context = {}
        email_field = self.model._meta.get_field(self.model.USERNAME_FIELD)
        defaults = {
            'auto_populated_fields': (),
            'username_help_text': email_field.help_text,
        }
        extra_context.update(defaults)
        return super(PostUserAdmin, self).add_view(request, form_url,
                                               extra_context)

    @sensitive_post_parameters_m
    def user_change_password(self, request, id, form_url=''):
        if not self.has_change_permission(request):
            raise PermissionDenied
        user = get_object_or_404(self.get_queryset(request), pk=id)
        if request.method == 'POST':
            form = self.change_password_form(user, request.POST)
            if form.is_valid():
                form.save()
                change_message = self.construct_change_message(request, form, None)
                self.log_change(request, user, change_message)
                msg = ugettext('Password changed successfully.')
                messages.success(request, msg)
                return HttpResponseRedirect('..')
        else:
            form = self.change_password_form(user)

        fieldsets = [(None, {'fields': list(form.base_fields)})]
        adminForm = admin.helpers.AdminForm(form, fieldsets, {})

        context = {
            'title': _('Change password: %s') % escape(user.get_username()),
            'adminForm': adminForm,
            'form_url': form_url,
            'form': form,
            'is_popup': IS_POPUP_VAR in request.REQUEST,
            'add': True,
            'change': False,
            'has_delete_permission': False,
            'has_change_permission': True,
            'has_absolute_url': False,
            'opts': self.model._meta,
            'original': user,
            'save_as': False,
            'show_save': True,
        }
        return TemplateResponse(request,
            self.change_user_password_template or
            'admin/auth/user/change_password.html',
            context, current_app=self.admin_site.name)

    def response_add(self, request, obj, post_url_continue=None):
        if '_addanother' not in request.POST and IS_POPUP_VAR not in request.POST:
            request.POST['_continue'] = 1
        return super(PostUserAdmin, self).response_add(request, obj,
                                                   post_url_continue)


admin.site.register(Post, PostAdmin)
admin.site.register(PostMeta, PostMetaAdmin)
admin.site.register(PostMetaInfo, PostMetaInfoAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Links, LinksAdmin)
admin.site.register(LinkGroup, LinkGroupAdmin)
admin.site.register(Config, ConfigAdmin)
admin.site.register(PostUser, PostUserAdmin)
