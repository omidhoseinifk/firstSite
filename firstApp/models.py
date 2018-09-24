# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


class PostsGroup(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Post Group')
        verbose_name_plural = _('Posts Group')


class Posts(models.Model):
    # posts_group = models.OneToOneField(PostsGroup)
    # posts_group = models.ManyToManyField(PostsGroup)
    # boolean = models.BooleanField()
    # null_boolean = models.NullBooleanField()
    # date_and_time = models.DateTimeField()
    # email = models.EmailField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(
        'owner'), blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = RichTextUploadingField(
        _('content'), config_name='default')
    file = models.FileField(
        _('upload file'), upload_to='files/%Y/%m/%d/%r',
        null=True, blank=True)
    image = models.ImageField(
        _('upload image'), upload_to='images/%Y/%m/%d/%r',
        null=True, blank=True)
    update_date_time = models.DateTimeField(
        _('create date'), auto_now_add=True, auto_now=False)
    create_date_time = models.DateTimeField(
        _('update date'), auto_now_add=False, auto_now=True)

    # def __unicode__(self):
    #     return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('firstApp:detail', kwargs={'id': self.id})

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
