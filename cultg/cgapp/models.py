from django.db import models
from django.utils import timezone
from easy_thumbnails.fields import ThumbnailerImageField
from tinymce.models import HTMLField

#News Model
class News(models.Model):
    name = models.CharField(max_length=200)
    body = HTMLField() 
    pub_date = models.DateTimeField(default=timezone.datetime.now)
    language = models.CharField(max_length=200)
    image = ThumbnailerImageField(upload_to='photos/blog', blank=True) 
    
    class Meta:
        ordering = ('-pub_date',)

#Members Model
class Member(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    description = HTMLField()
    pub_date = models.DateTimeField(default=timezone.now)
    language = models.CharField(max_length=200)
    image = ThumbnailerImageField(upload_to='photos/members', blank=True) 

    class Meta:
        ordering = ('-pub_date',)

#Projects Model
class Project(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = HTMLField()
    pub_date = models.DateTimeField(default=timezone.now)
    language = models.CharField(max_length=200)
    image = ThumbnailerImageField(upload_to='photos/projects', blank=True) 

    class Meta:
        ordering = ('-pub_date',)

#Partners Model
class Partner(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(default=timezone.now)
    language = models.CharField(max_length=200)
    image = ThumbnailerImageField(upload_to='photos/partners', blank=True) 
