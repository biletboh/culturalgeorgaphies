from django.shortcuts import render

from django.views.generic import View, DetailView, ListView, FormView, TemplateView, DeleteView 
from django.views.generic.edit import FormMixin

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from cgapp.models import Member, News, Project, Partner

from django.contrib.auth.models import User
from cgapp.forms import NewsForm, MemberForm, ProjectForm, PartnerForm 

from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse, reverse_lazy
from django.http import HttpResponseForbidden
from django.views.generic.detail import SingleObjectMixin

#Blog
class Blog(ListView):
    model = News
    template_name = 'cgapp/blog.html'
    def get_context_data(self, **kwargs):
        context = super(Blog, self).get_context_data(**kwargs)
        context['partners'] = Partner.objects.all()
        return context

#News page
class NewsPage(DetailView):
    model = News
    template_name = 'cgapp/news.html'
    def get_context_data(self, **kwargs):
        context = super(NewsPage, self).get_context_data(**kwargs)
        context['partners'] = Partner.objects.all()
        return context

#About page
class About(TemplateView):
    template_name = 'cgapp/about.html'
    def get_context_data(self, **kwargs):
        context = super(About, self).get_context_data(**kwargs)
        context['partners'] = Partner.objects.all()
        return context

#Team page
class Team(ListView):
    model = Member
    template_name = 'cgapp/team.html'
    def get_context_data(self, **kwargs):
        context = super(Team, self).get_context_data(**kwargs)
        context['partners'] = Partner.objects.all()
        return context

#Member page
class Members(DetailView):
    model = Member
    template_name = 'cgapp/members.html'
    def get_context_data(self, **kwargs):
        context = super(Members, self).get_context_data(**kwargs)
        context['partners'] = Partner.objects.all()
        return context

#Projects page
class Projects(ListView):
    model = Project
    template_name = 'cgapp/projects.html'
    def get_context_data(self, **kwargs):
        context = super(Projects, self).get_context_data(**kwargs)
        context['partners'] = Partner.objects.all()
        return context

#Project Detail page
class ProjectDetails(DetailView):
    model = Project
    template_name = 'cgapp/project-page.html'
    def get_context_data(self, **kwargs):
        context = super(ProjectDetails, self).get_context_data(**kwargs)
        context['partners'] = Partner.objects.all()
        return context

###Dashboard 

#Create News page
class CreateNews(FormView):
    form_class = NewsForm 
    template_name = 'cgapp/create.html'
    success_url = '/dashboard/news/add/'
    def form_valid(self, form):
        news = News(name=form.cleaned_data['name'], body=form.cleaned_data['body'], image=form.cleaned_data['image'])
        news.save()
        form.delete_temporary_files()
        return super(CreateNews, self).form_valid(form)

#Edit list of News
class NewsEditList(ListView):
    model = News  
    template_name = 'cgapp/editlist.html'
    def get_context_data(self, **kwargs):
        context = super(NewsEditList, self).get_context_data(**kwargs)
        context['edit_url'] = 'cgapp:edit-news'
        context['delete_url'] = 'cgapp:delete-news'
        return context

#Delete News page
class DeleteNews(DeleteView):
    model = News
    template_name = 'cgapp/editlist.html'
    success_url = 'dashboard/news/list/' 

#Edit News Page
class DisplayNews(DetailView):
    template_name = 'cgapp/edit.html'
    model = News
    def get_context_data(self, **kwargs):
        context = super(DisplayNews, self).get_context_data(**kwargs)
        context['form'] = NewsForm()
        return context

class UpdateNews(SingleObjectMixin, FormView):
    form_class = NewsForm 
    model = News 

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(UpdateNews, self).post(request, *args, **kwargs)
 
    def form_valid(self, form):
        #obtain current object 
        params = { 'pk': form.cleaned_data['object_id'] }
        news = News.objects.get(**params)
        news.name = form.cleaned_data['name'] 
        news.description=form.cleaned_data['body'] 
        image=form.cleaned_data['image']
        if image: 
            news.image = image
        news.save()

        form.delete_temporary_files()
        return super(UpdateNews, self).form_valid(form)

    def get_success_url(self):
        return reverse('cgapp:edit-news', kwargs={'pk': self.object.pk})

class EditNews(View):
    def get(self, request, *args, **kwargs):
        view = DisplayNews.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = UpdateNews.as_view()
        return view(request, *args, **kwargs)

#Create Member page
class CreateMember(FormView):
    form_class = MemberForm 
    template_name = 'cgapp/create.html'
    success_url = '/dashboard/members/add/'
    def form_valid(self, form):
        members = Member(first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'], description=form.cleaned_data['description'], image=form.cleaned_data['image'])
        members.save()
        form.delete_temporary_files()
        return super(CreateMember, self).form_valid(form)
    
#Edit list of Member 
class MemberEditList(ListView):
    model = Member 
    template_name = 'cgapp/editlist.html'
    def get_context_data(self, **kwargs):
        context = super(MemberEditList, self).get_context_data(**kwargs)
        context['edit_url'] = 'cgapp:edit-member'
        context['delete_url'] = 'cgapp:delete-member'
        return context

#Delete Member page
class DeleteMember(DeleteView):
    model = Member
    template_name = 'cgapp/delete-member.html'
    success_url = 'dashboard/members/list/' 

#Edit Member Page
class DisplayMember(DetailView):
    template_name = 'cgapp/edit.html'
    model = Member 
    def get_context_data(self, **kwargs):
        context = super(DisplayMember, self).get_context_data(**kwargs)
        context['form'] = MemberForm()
        return context

class UpdateMember(SingleObjectMixin, FormView):
    form_class = MemberForm 
    model = Member 

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(UpdateMember, self).post(request, *args, **kwargs)
    
    def form_valid(self, form):
        #obtain current object 
        params = { 'pk': form.cleaned_data['object_id'] }
        member = Member.objects.get(**params)

        member.first_name=form.cleaned_data['first_name'] 
        member.last_name=form.cleaned_data['last_name'] 
        member.description=form.cleaned_data['description'] 
        image=form.cleaned_data['image']
        if image: 
            member.image = image
        member.save()

        form.delete_temporary_files()
        return super(UpdateMember, self).form_valid(form)

    def get_success_url(self):
        return reverse('cgapp:edit-member', kwargs={'pk': self.object.pk})

class EditMember(View):
    def get(self, request, *args, **kwargs):
        view = DisplayMember.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = UpdateMember.as_view()
        return view(request, *args, **kwargs)

#Create Project page
class CreateProject(FormView):
    form_class = ProjectForm
    template_name = 'cgapp/create.html'
    success_url = '/dashboard/projects/add/'
    def form_valid(self, form):
        project = Project(name=form.cleaned_data['name'], description=form.cleaned_data['description'], category=form.cleaned_data['category'], image=form.cleaned_data['image'])
        project.save()
        form.delete_temporary_files()
        return super(CreateProject, self).form_valid(form)
    
#Edit list of Projects 
class ProjectsEditList(ListView):
    model = Project 
    template_name = 'cgapp/editlist.html'
    def get_context_data(self, **kwargs):
        context = super(ProjectsEditList, self).get_context_data(**kwargs)
        context['edit_url'] = 'cgapp:edit-project'
        context['delete_url'] = 'cgapp:delete-project'
        return context

#Delete Project page
class DeleteProject(DeleteView):
    model = Project 
    template_name = 'cgapp/delete-project.html'
    success_url = '/dashboard/projects/list/'

#Edit Project Page
class DisplayProject(DetailView):
    template_name = 'cgapp/edit.html'
    model = Project 
    def get_context_data(self, **kwargs):
        context = super(DisplayProject, self).get_context_data(**kwargs)
        context['form'] = ProjectForm()
        return context

class UpdateProject(SingleObjectMixin, FormView):
    form_class = ProjectForm 
    model = Project

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(UpdateProject, self).post(request, *args, **kwargs)
    
    def form_valid(self, form):
        #obtain current object 
        params = { 'pk': form.cleaned_data['object_id'] }
        project = Project.objects.get(**params)

        project.name=form.cleaned_data['name'] 
        project.category=form.cleaned_data['category'] 
        project.description=form.cleaned_data['description'] 
        image=form.cleaned_data['image']
        if image: 
            project.image = image
        project.save()

        form.delete_temporary_files()
        return super(UpdateProject, self).form_valid(form)

    def get_success_url(self):
        return reverse('cgapp:edit-project', kwargs={'pk': self.object.pk})

class EditProject(View):
    def get(self, request, *args, **kwargs):
        view = DisplayProject.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = UpdateProject.as_view()
        return view(request, *args, **kwargs)

#Create Partner Icon
class CreatePartner(SuccessMessageMixin, FormView):
    form_class = PartnerForm 
    template_name = 'cgapp/create.html'
    success_url = '/dashboard/partner/add/'
    success_message = "Partner was created successfully"
    def form_valid(self, form):
        partner = Partner(name=form.cleaned_data['name'], image=form.cleaned_data['image'])
        partner.save()
        form.delete_temporary_files()
        return super(CreatePartner, self).form_valid(form)

#Edit list of Partners 
class PartnersEditList(ListView):
    model = Partner 
    template_name = 'cgapp/editlist.html'
    def get_context_data(self, **kwargs):
        context = super(PartnersEditList, self).get_context_data(**kwargs)
        context['edit_url'] = 'cgapp:edit-partner'
        context['delete_url'] = 'cgapp:delete-partner'
        return context

#Delete Parnter page
class DeletePartner(DeleteView):
    model = Partner 
    success_url = '/dashboard/partners/list/'

#Edit Partner Page
class DisplayPartner(DetailView):
    template_name = 'cgapp/edit.html'
    model = Partner 
    def get_context_data(self, **kwargs):
        context = super(DisplayPartner, self).get_context_data(**kwargs)
        context['form'] = PartnerForm()
        return context

class UpdatePartner(SingleObjectMixin, FormView):
    form_class = PartnerForm 
    model = Partner 

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(UpdatePartner, self).post(request, *args, **kwargs)
    
    def form_valid(self, form):
        #obtain current object 
        params = { 'pk': form.cleaned_data['object_id'] }
        partner = Partner.objects.get(**params)

        partner.name=form.cleaned_data['name'] 
        image=form.cleaned_data['image']
        if image: 
            partner.image = image
        partner.save()

        form.delete_temporary_files()
        return super(UpdatePartner, self).form_valid(form)

    def get_success_url(self):
        return reverse('cgapp:edit-partner', kwargs={'pk': self.object.pk})

class EditPartner(View):
    def get(self, request, *args, **kwargs):
        view = DisplayPartner.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = UpdatePartner.as_view()
        return view(request, *args, **kwargs)

