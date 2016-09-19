# coding=utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


# 用户模型(采用继承方式扩展用户信息)
class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar')
    qq = models.CharField(max_length=20, blank=True, verbose_name='QQ')
    mobile = models.CharField(max_length=11, blank=True, null=True, verbose_name='电话号码')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.username


# tag(标签)
class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='标签名称')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        # 必须返回字符串
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)
    index = models.IntegerField()

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        # 必须返回字符串
        return self.name


class ArticalAdmin(models.Manager):
    def distinct_date(self):
        distinct_date_list = []
        date_list = self.values('date_publish')
        for date in date_list:
            date = date['date_publish'].strftime('%Y/%m文章存档')
            if date not in distinct_date_list:
                distinct_date_list.append(date)
        return distinct_date_list


class Artical(models.Model):
    title = models.CharField('文章标题', max_length=50)
    desc = models.CharField('文章描述', max_length=50)
    content = models.TextField('文章内容')
    click_count = models.IntegerField('点击次数', default=0)
    is_recommend = models.BooleanField('是否推荐', default=False)
    date_publish = models.DateTimeField(verbose_name='发布时间')
    user = models.ForeignKey(User, verbose_name='用户')
    category = models.ForeignKey(Category, verbose_name='分类')
    tag = models.ManyToManyField(Tag, verbose_name=u'标签')

    objects = ArticalAdmin()

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __unicode__(self):
        # 必须返回字符串
        return self.title


class Comment(models.Model):
    content = models.TextField('评论内容')
    date_publish = models.DateTimeField('发布时间', auto_now_add=True)
    artical = models.ForeignKey(Artical, blank=True, null=True, verbose_name='文章')
    pid = models.ForeignKey('self', blank=True, null=True, verbose_name='父级评论')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __unicode__(self):
        # 必须返回字符串
        return str(self.id)


# 友情链接
class Links(models.Model):
    title = models.CharField('标题', max_length=50)
    description = models.CharField('友情链接描述', max_length=200)
    callback_url = models.DateTimeField('URL地址')
    date_publish = models.DateTimeField('发布时间', auto_now_add=True)
    index = models.IntegerField('排序顺序（从小到大）', default=999)

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __unicode__(self):
        # 必须返回字符串
        return self.title


# 广告
class Ad(models.Model):
    title = models.CharField('广告标题', max_length=50)
    description = models.CharField('广告描述', max_length=200)
    image_url = models.ImageField(upload_to='ad/%Y/%m', verbose_name='图片路径')
    callback_url = models.URLField(null=True, blank=True, verbose_name='回调url')
    date_publish = models.DateTimeField('发布时间', auto_now_add=True)
    index = models.IntegerField(default=999, verbose_name='排序顺序（从小到大）')

    class Meta:
        verbose_name = '广告'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __unicode__(self):
        # 必须返回字符串
        return self.title

