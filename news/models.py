from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from datetime import datetime
import re
import availability

SUMMARY_MAX_LENGTH = 768

MARKUP_FILTER_CHOICES = []

# Loops through each filter in the dict of possible markup filters and maps them to choices.
filters_iter = availability.markup_filters.iterkeys()
for index in xrange(len(availability.markup_filters)):
    current_filter = filters_iter.next()

    if availability.markup_filters[current_filter] is True:
        MARKUP_FILTER_CHOICES.append( (index,current_filter) )

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
    markup_filter = models.PositiveIntegerField(max_length=32, choices=MARKUP_FILTER_CHOICES, null=True, blank=True)
    slug = models.SlugField(blank=True, unique=True)
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,null=True,blank=True)
    category = models.ManyToManyField(Category,related_name='articles',null=True,blank=True)

    def formatted_summary(self):
        return self.formatted_body(summary=True)

    def formatted_body(self, summary=False):
        from django.contrib.markup.templatetags import markup

        if summary:
            body = self.summary
        else:
            body = self.body

        if self.markup_filter is not None and self.get_markup_filter_display() in availability.markup_filters:

            markup_method = getattr(markup, self.get_markup_filter_display())

            return markup_method(body)
        else:
            return body

    @models.permalink
    def get_absolute_url(self):
        return ('news_article', [str(self.id)])

    def save(self, *args, **kwargs):
        if not self.summary:
            if len(self.body) > SUMMARY_MAX_LENGTH:
                self.summary = self.body[0:(SUMMARY_MAX_LENGTH-1)]
            else:
                self.summary = self.body

        if not self.created:
            self.created = datetime.now()
        self.slug = ('%s-%s' % (self.created.strftime('%Y-%m-%d'), slugify(self.title)))[:50]

        super(Article,self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

