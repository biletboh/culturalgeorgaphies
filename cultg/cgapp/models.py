from django.db import models
from django.utils import timezone
# Create your models here.

class News(models.Model):
    name = models.CharField(max_length=200)
    body = models.CharField(max_length=6000)
    pub_date = models.DateTimeField(default=timezone.now)

class Member(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    description = models.CharField(max_length=1500)

    #def get_absolute_url(self):
    #    return reverse('members', kwargs={'pk': self.pk})

class Project(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.CharField(max_length=2500)
