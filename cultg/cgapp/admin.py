from django.contrib import admin

# Register your models here.
from .models import News, Member, Project 

class ArticleAdmin(admin.ModelAdmin):
    class Media:
        js = ['/path/to/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/path/to/your/tinymce_setup.js']

admin.site.register(News, Member, Project, ArticleAdmin)
