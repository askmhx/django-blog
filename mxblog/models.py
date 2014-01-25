from datetime import datetime
from ckeditor.fields import RichTextField
from django.db import models


class CommonInfo(models.Model):
    update_time = models.DateTimeField(default=datetime.now)
    create_time = models.DateTimeField(default=datetime.now)

    class Meta:
        abstract = True
        ordering = ['-create_time']

class User(CommonInfo):
    login_id = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    username = models.CharField(max_length=20, blank=True)
    # avatar = models.ImageField(max_length=100, upload_to=os.path.join(os.path.dirname(__file__), '..', 'static/afiles').replace('\\', '/'))
    email = models.EmailField(max_length=20, blank=True)
    mobile = models.CharField(max_length=11, blank=True)
    website = models.URLField(max_length=255, blank=True)
    login_count = models.BigIntegerField(default=0)
    last_login_ip = models.CharField(max_length=32, blank=True)
    last_login_time = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return self.username

    class Meta(CommonInfo.Meta):
        db_table = 't_user'


class BlogGroup(CommonInfo):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, blank=True)

    def __unicode__(self):
        return self.title

    class Meta(CommonInfo.Meta):
        db_table = 't_blog_group'


class Blog(CommonInfo):
    title = models.CharField(max_length=100)
    content = RichTextField()
    tags = models.CharField(max_length=100)
    author = models.ForeignKey(User, blank=True)
    group = models.ForeignKey(BlogGroup, blank=True)
    support = models.BigIntegerField(default=0)
    oppose = models.BigIntegerField(default=0)

    def __unicode__(self):
        return self.title

    class Meta(CommonInfo.Meta):
        db_table = 't_blog'



class SiteConfig(CommonInfo):
    info_title = models.CharField(max_length=100)
    info_key = models.CharField(max_length=30)
    info_value = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.info_key

    class Meta(CommonInfo.Meta):
        db_table = 't_site_config'
