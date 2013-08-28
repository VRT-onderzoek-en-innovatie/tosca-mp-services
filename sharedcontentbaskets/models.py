from django.db import models

# Create your models here.
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class ContentID(models.Model):
    contentid = models.CharField(max_length=100, blank=False, default='', unique=True)

class UserName(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)

class SharedContentBasket(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='', unique=True)
    users = models.ManyToManyField(UserName, related_name='sharedcontentbaskets')
    content = models.ManyToManyField(ContentID, blank=True, related_name='sharedcontentbaskets')
    # TODO: segment of content
