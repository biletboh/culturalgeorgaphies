from django.contrib import admin

# Register your models here.
from .models import News, Member, Project 

class ArticleAdmin(admin.ModelAdmin):
    class Media:
        js = ['/static/tiny_mce/tiny_mce.js',]

admin.site.register(News, ArticleAdmin)
admin.site.register(Member, ArticleAdmin)
admin.site.register(Project, ArticleAdmin)
