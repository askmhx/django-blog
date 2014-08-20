# coding=utf-8
from datetime import datetime
import os

from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class PostUserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, is_staff=is_staff, is_active=True, is_superuser=is_superuser, last_login=now,create_time=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class PostUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name=u"邮件", unique=True, db_index=True)
    username = models.CharField(verbose_name=u"名字", max_length=30, db_index=True)
    avatar = models.ImageField(verbose_name=u"头像", blank=True, max_length=100, upload_to=os.path.join(os.path.dirname(__file__), '..', 'static/ufiles').replace('\\', '/'))
    mobile = models.CharField(verbose_name=u"手机", max_length=11, blank=True)
    site = models.URLField(verbose_name=u"网站", max_length=255, blank=True)
    bio = models.URLField(verbose_name=u"签名", max_length=255, blank=True)
    login_count = models.IntegerField(verbose_name=u"登录次数", default=0)
    last_ip = models.CharField(verbose_name=u"最后登录IP", max_length=32, blank=True)
    birthday = models.DateField(verbose_name=u"生日", blank=True, default='1900-01-01')
    is_staff = models.BooleanField(verbose_name=u"后台权限", default=False)
    is_active = models.BooleanField(verbose_name=u"是否启用", default=True)
    update_time = models.DateTimeField(verbose_name=u"更新时间", default=datetime.now)
    create_time = models.DateTimeField(verbose_name=u"创建时间", default=datetime.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = PostUserManager()

    def get_full_name(self):
        return '%s(%s)' % (self.email, self.username)

    def get_short_name(self):
        return self.email

    def __unicode__(self):
        return self.email

    class Meta:
        db_table = 'mx_user'
        ordering = ['-update_time']
        verbose_name = u'用户'
        verbose_name_plural = u'用户'


class ModelMeta(models.Model):
    update_time = models.DateTimeField(verbose_name=u"更新时间", default=datetime.now)
    create_time = models.DateTimeField(verbose_name=u"创建时间", default=datetime.now)

    class Meta:
        abstract = True
        ordering = ['-create_time']


class PostMeta(ModelMeta):
    title = models.CharField(verbose_name=u"名称", max_length=200)
    author = models.ForeignKey(PostUser, verbose_name=u"作者", blank=True)
    type = models.IntegerField(verbose_name=u"类型", max_length=1)

    def __unicode__(self):
        return self.title

    class Meta(ModelMeta.Meta):
        db_table = 'mx_post_meta'
        verbose_name = u'属性名称'
        verbose_name_plural = u'属性名称'
        app_label = u"发布文章"


class Post(ModelMeta):
    title = models.CharField(verbose_name=u"主题", max_length=100)
    content = RichTextField(verbose_name=u"内容")
    author = models.ForeignKey(PostUser, verbose_name=u"作者", blank=True)
    support = models.BigIntegerField(verbose_name=u"支持", default=0)
    oppose = models.BigIntegerField(verbose_name=u"反对", default=0)

    def __unicode__(self):
        return self.title

    class Meta(ModelMeta.Meta):
        db_table = 'mx_post'
        verbose_name = u'发布'
        verbose_name_plural = u'发布'
        app_label = u"发布文章"


class PostMetaInfo(ModelMeta):
    post = models.ForeignKey(Post, verbose_name=u"主题")
    meta = models.ForeignKey(PostMeta, verbose_name=u"属性")

    def __unicode__(self):
        return self.post

    class Meta(ModelMeta.Meta):
        db_table = 'mx_post_meta_info'
        verbose_name = u'分组/标注'
        verbose_name_plural = u'分组/标注'
        app_label = u"发布文章"


class Comments(ModelMeta):
    parent = models.IntegerField(verbose_name=u"上级", blank=type)
    post = models.ForeignKey(Post, verbose_name=u"主题",  blank=True)
    author = models.ForeignKey(PostUser, verbose_name=u"作者", blank=True)
    content = models.CharField(verbose_name=u"内容", max_length=1000)
    ip = models.GenericIPAddressField(verbose_name=u"IP", max_length=100)

    def __unicode__(self):
        return self.content

    class Meta(ModelMeta.Meta):
        db_table = 'mx_comments'
        verbose_name = u'留言'
        verbose_name_plural = u'留言'
        app_label = u"留言信息"


class LinkGroup(ModelMeta):
    title = models.CharField(verbose_name=u"名称", max_length=100)
    author = models.ForeignKey(PostUser, verbose_name=u"作者",  blank=True)

    def __unicode__(self):
        return self.title

    class Meta(ModelMeta.Meta):
        db_table = 'mx_link_group'
        verbose_name = u'链接分组'
        verbose_name_plural = u'链接分组'
        app_label = u"链接信息"


class Links(ModelMeta):
    url = models.URLField(verbose_name=u"URL", max_length=100)
    title = models.CharField(verbose_name=u"名称", max_length=30)
    image = models.ImageField(verbose_name=u"图片", blank=True)
    description = models.CharField(verbose_name=u"简介", max_length=1000)
    owner = models.CharField(verbose_name=u"主人", max_length=1000)
    rating = models.IntegerField(verbose_name=u"评分", default=0)
    group = models.ForeignKey(LinkGroup, verbose_name=u"分组", blank=True)
    visible = models.BooleanField(verbose_name=u"显示", default=True)
    highlight = models.BooleanField(verbose_name=u"高亮", default=False)

    def __unicode__(self):
        return self.title

    class Meta(ModelMeta.Meta):
        db_table = 'mx_links'
        verbose_name = u'链接'
        verbose_name_plural = u'链接'
        app_label = u"链接信息"


class Config(ModelMeta):
    info_title = models.CharField(verbose_name=u"名称", max_length=100)
    info_key = models.CharField(verbose_name=u"键", max_length=30)
    info_value = models.CharField(verbose_name=u"值", max_length=1000)

    def __unicode__(self):
        return self.info_title

    class Meta(ModelMeta.Meta):
        db_table = 'mx_config'
        verbose_name = u'设置'
        verbose_name_plural = u'设置'
        app_label = u"网站设置"



