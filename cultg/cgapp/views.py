from django.shortcuts import render

from django.views.generic import View, DetailView, TemplateView 

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from cgapp.models import Member 

from django.contrib.auth.models import User

#News page
class News(TemplateView):
    template_name = 'cgapp/news.html'

#About page
class About(TemplateView):
    template_name = 'cgapp/about.html'

#Team page
class Team(TemplateView):
    template_name = 'cgapp/team.html'

#Member page
class Members(TemplateView):
    template_name = 'cgapp/members.html'

#Projects page
class Projects(TemplateView):
    template_name = 'cgapp/projects.html'

#Project Detail page
class ProjectDetail(TemplateView):
    template_name = 'cgapp/project-page.html'

#Gallery page 
class Gallery(TemplateView):
    template_name = 'cgapp/gallery.html'


###Dashboard 

#Create News page
class CreateNews(TemplateView):
    template_name = 'cgapp/create-news.html'

#Delete News page
class DeleteNews(TemplateView):
    template_name = 'cgapp/delete-news.html'

#Edit News Page
class EditNews(TemplateView):
    template_name = 'cgapp/edit-news.html'

#Create Member page/Dashboard
class CreateMember(CreateView):
    model = Member
    fields = ['name', 'description']
    template_name = 'cgapp/create-member.html'
    print('hello')

#Delete Member page
class DeleteMember(DeleteView):
    model = Member
    template_name = 'cgapp/delete-member.html'

#Edit Member Page
class EditMember(UpdateView):
    model = Member
    fields = ['name', 'description']
    template_name = 'cgapp/edit-member.html'
    success_url = reverse_lazy('cgapp:members')

