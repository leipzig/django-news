from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from datetime import datetime
from . import availability


class Category(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True)
    name = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        if not self.parent:
            return self.name

        return '%s of %s' % self.name, self.parent.name


class Article(models.Model):
    """A single news entry."""

    class Meta(object):
        ordering = ['-created']

    title = models.CharField(max_length=64)
    body = models.TextField()
    summary = models.TextField(blank=True)
    slug = models.SlugField(blank=True, unique=True)
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, null=True, blank=True)
    category = models.ManyToManyField(Category, related_name='articles', null=True, blank=True)

    def formatted_summary(self):
        return self.formatted_body(summary=True)

    def formatted_body(self, summary=False):

        if summary:
            body = self.summary
        else:
            body = self.body

        return body

    @models.permalink
    def get_absolute_url(self):
        return 'news_article', [str(self.id)]

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = datetime.now()
        self.slug = ('news-%s-%s' % (self.created.strftime('%Y-%m-%d'), slugify(self.title)))[:50]

        super(Article, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title
