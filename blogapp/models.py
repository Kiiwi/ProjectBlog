import os

from django.db import models
from django.core.urlresolvers import reverse


def get_upload_path(instance, filename):
    return os.path.join(
        "%s" % instance.title, filename)


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    teaser = models.TextField('teaser', blank=True)
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(upload_to=get_upload_path, blank=True)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return reverse('blogapp.views.post', args=[self.slug])


class Image(models.Model):
    image = models.ImageField(upload_to=get_upload_path, blank=True)
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return u'%s' % self.title
