from django.db import models

# Create your models here.

class News(models.Model):
    name = models.CharField(max_length=200)
    body = models.CharField(max_length=6000)
    pub_date = models.DateTimeField('date published')

class Member(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1500)

    #def get_absolute_url(self):
    #    return reverse('members', kwargs={'pk': self.pk})

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2500)
