from django.db import models
from django.utils import timezone
from easy_thumbnails.fields import ThumbnailerImageField
from tinymce.models import HTMLField
# Create your models here.

class News(models.Model):
    name = models.CharField(max_length=200)
    body = models.CharField(max_length=6000)
    pub_date = models.DateTimeField(default=timezone.now)
    language = models.CharField(max_length=200)
    image = ThumbnailerImageField(upload_to='photos/blog', blank=True) 

class Member(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    description = models.CharField(max_length=1500)
    language = models.CharField(max_length=200)
    image = ThumbnailerImageField(upload_to='photos/members', blank=True) 

    #def get_absolute_url(self):
    #    return reverse('members', kwargs={'pk': self.pk})

class Project(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.CharField(max_length=2500)
    language = models.CharField(max_length=200)
    image = ThumbnailerImageField(upload_to='photos/projects', blank=True) 

class Partner(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2500)
    language = models.CharField(max_length=200)
    image = ThumbnailerImageField(upload_to='photos/projects', blank=True) 
