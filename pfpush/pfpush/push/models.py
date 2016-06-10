from __future__ import unicode_literals

from django.db import models

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# Create your models here.
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Push(models.Model):
    sendtime = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=10, blank=True, default='')
    target = models.CharField(max_length=10, blank=True, default='')
    title = models.TextField()
    content = models.TextField()

    class Meta:
        ordering = ('sendtime',)

class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=10, blank=True, default='')
    token = models.CharField(max_length=500, blank=True, default='')

    class Meta :
        ordering = ('created',)