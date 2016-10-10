from django.shortcuts import render

from django.views.generic import View, DetailView, ListView, FormView, TemplateView 
from django.views.generic.edit import FormMixin

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from cgapp.models import Member, News, Project

from django.contrib.auth.models import User
from cgapp.forms import NewsForm, MemberForm, ProjectForm 

#Blog
class Blog(ListView):
    model = News
    template_name = 'cgapp/blog.html'

#News page
class NewsPage(DetailView):
    model = News
    template_name = 'cgapp/news.html'

#About page
class About(TemplateView):
    template_name = 'cgapp/about.html'

#Team page
class Team(ListView):
    model = Member
    template_name = 'cgapp/team.html'

#Member page
class Members(DetailView):
    model = Member
    template_name = 'cgapp/members.html'

#Projects page
class Projects(ListView):
    model = Project
    template_name = 'cgapp/projects.html'

#Project Detail page
class ProjectDetails(DetailView):
    model = Project
    template_name = 'cgapp/project-page.html'

#Gallery page 
class Gallery(TemplateView):
    template_name = 'cgapp/gallery.html'


###Dashboard 

#Create News page
class CreateNews(FormView):
    form_class = NewsForm 
    template_name = 'cgapp/create.html'
    success_url = '/dashboard/news/add/'
    def form_valid(self, form):
        news = News(name=form.cleaned_data['name'], body=form.cleaned_data['body'], picture=form.cleaned_data['picture'])
        news.save()
        form.delete_temporary_files()
        return super(CreateNews, self).form_valid(form)
    
#Delete News page
class DeleteNews(TemplateView):
    template_name = 'cgapp/delete-news.html'

#Edit News Page
class EditNews(TemplateView):
    template_name = 'cgapp/edit-news.html'

#Create Member page/Dashboard
class CreateMember(FormView):
    form_class = MemberForm 
    template_name = 'cgapp/create.html'
    success_url = '/dashboard/members/add/'
    def form_valid(self, form):
        members = Member(first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'], description=form.cleaned_data['description'], avatar=form.cleaned_data['avatar'])
        members.save()
        form.delete_temporary_files()
        return super(CreateMember, self).form_valid(form)
    

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

#Create Project page/Dashboard
class CreateProject(FormView):
    form_class = ProjectForm
    template_name = 'cgapp/create.html'
    success_url = '/dashboard/'
    def form_valid(self, form):
        project = Project(name=form.cleaned_data['name'], description=form.cleaned_data['description'], category=form.cleaned_data['category'], image=form.cleaned_data['image'])
        project.save()
        form.delete_temporary_files()
        return super(CreateProject, self).form_valid(form)

#Delete Member page
class DeleteProject(DeleteView):
    model = Project 
    template_name = 'cgapp/delete-project.html'

#Edit Member Page
class EditProject(UpdateView):
    model = Project 
    fields = ['name', 'description']
    template_name = 'cgapp/edit-project.html'
    success_url = reverse_lazy('cgapp:projects')

