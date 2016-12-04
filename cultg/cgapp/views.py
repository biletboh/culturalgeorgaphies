from django.shortcuts import render

from django.views.generic import View, DetailView, ListView, FormView, TemplateView, DeleteView 

from el_pagination.views import AjaxListView

from django.views.generic.edit import FormMixin

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from cgapp.models import Member, News, Project, Partner

from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import authenticate, login
from cgapp.forms import NewsForm, MemberForm, ProjectForm, PartnerForm 

from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse, reverse_lazy
from django.http import HttpResponseForbidden
from django.views.generic.detail import SingleObjectMixin

from django.utils.translation import ugettext_lazy as _

#Blog
class Blog(AjaxListView):
    context_object_name = "posts"
    template_name = 'cgapp/blog.html'
    page_template = 'cgapp/post_list.html'
    def get_context_data(self, **kwargs):
        context = super(Blog, self).get_context_data(**kwargs)
        context['partners'] = Partner.objects.all()
        return context
    def get_queryset(self):
        return News.objects.all()

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
class CreateNews(SuccessMessageMixin, LoginRequiredMixin, FormView):
    form_class = NewsForm 
    template_name = 'cgapp/create.html'
    success_url = '/dashboard/news/add/'
    login_url = '/dashboard/'
    success_message = _("A post was created successfully")
    def form_valid(self, form):
        news = News(name=form.cleaned_data['name'], language=form.cleaned_data['language'], pub_date=form.cleaned_data['pub_date'], body=form.cleaned_data['body'], image=form.cleaned_data['image'])
        news.save()
        form.delete_temporary_files()
        return super(CreateNews, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateNews, self).get_context_data(**kwargs)
        context['title'] = _('News')
        return context   


#Edit list of News
class NewsEditList(LoginRequiredMixin, ListView):
    model = News  
    template_name = 'cgapp/editlist.html'
    login_url = '/dashboard/'
    def get_context_data(self, **kwargs):
        context = super(NewsEditList, self).get_context_data(**kwargs)
        context['edit_url'] = 'cgapp:edit-news'
        context['delete_url'] = 'cgapp:delete-news'
        context['title'] = _('News') 
        return context

#Delete News page
class DeleteNews(LoginRequiredMixin, DeleteView):
    model = News
    template_name = 'cgapp/editlist.html'
    success_url = 'dashboard/news/list/' 

#Edit News Page
class DisplayNews(LoginRequiredMixin, DetailView):
    template_name = 'cgapp/edit.html'
    login_url = '/dashboard/'
    model = News
    def get_context_data(self, **kwargs):
        context = super(DisplayNews, self).get_context_data(**kwargs)
        context['form'] = NewsForm()
        context['title'] = _('News') 
        return context

class UpdateNews(SuccessMessageMixin, SingleObjectMixin, FormView):
    form_class = NewsForm 
    model = News 
    success_message = _("A post was updated successfully")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(UpdateNews, self).post(request, *args, **kwargs)
 
    def form_valid(self, form):
        #obtain current object 
        params = { 'pk': form.cleaned_data['object_id'] }
        news = News.objects.get(**params)
        news.name = form.cleaned_data['name'] 
        news.language=form.cleaned_data['language']
        news.pub_date=form.cleaned_data['pub_date']
        news.body = form.cleaned_data['body'] 
        image = form.cleaned_data['image']
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
class CreateMember(SuccessMessageMixin, LoginRequiredMixin, FormView):
    form_class = MemberForm 
    template_name = 'cgapp/create.html'
    success_url = '/dashboard/members/add/'
    login_url = '/dashboard/'
    success_message = _("A member was created successfully")
    def form_valid(self, form):
        members = Member(name=form.cleaned_data['name'], position=form.cleaned_data['position'], language=form.cleaned_data['language'], pub_date=form.cleaned_data['pub_date'], description=form.cleaned_data['description'], image=form.cleaned_data['image'])
        members.save()
        form.delete_temporary_files()
        return super(CreateMember, self).form_valid(form)
 
    def get_context_data(self, **kwargs):
        context = super(CreateMember, self).get_context_data(**kwargs)
        context['title'] = _('Members')
        return context   

#Edit list of Member 
class MemberEditList(LoginRequiredMixin, ListView):
    model = Member 
    template_name = 'cgapp/editlist.html'
    login_url = '/dashboard/'
    def get_context_data(self, **kwargs):
        context = super(MemberEditList, self).get_context_data(**kwargs)
        context['edit_url'] = 'cgapp:edit-member'
        context['delete_url'] = 'cgapp:delete-member'
        context['title'] = _('Members') 
        return context

#Delete Member page
class DeleteMember(LoginRequiredMixin, DeleteView):
    model = Member
    template_name = 'cgapp/delete-member.html'
    success_url = 'dashboard/members/list/' 

#Edit Member Page
class DisplayMember(LoginRequiredMixin, DetailView):
    template_name = 'cgapp/edit.html'
    login_url = '/dashboard/'
    model = Member 
    def get_context_data(self, **kwargs):
        context = super(DisplayMember, self).get_context_data(**kwargs)
        context['form'] = MemberForm()
        context['title'] = _('Members') 
        return context

class UpdateMember(SuccessMessageMixin, SingleObjectMixin, FormView):
    form_class = MemberForm 
    model = Member 
    success_message = _("A member was updated successfully")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(UpdateMember, self).post(request, *args, **kwargs)
    
    def form_valid(self, form):
        #obtain current object 
        params = { 'pk': form.cleaned_data['object_id'] }
        member = Member.objects.get(**params)

        member.name=form.cleaned_data['name'] 
        member.position=form.cleaned_data['position'] 
        member.language=form.cleaned_data['language']
        member.pub_date=form.cleaned_data['pub_date']
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
class CreateProject(SuccessMessageMixin, LoginRequiredMixin, FormView):
    form_class = ProjectForm
    template_name = 'cgapp/create.html'
    success_url = '/dashboard/projects/add/'
    login_url = '/dashboard/'
    success_message = _("A project was created successfully")

    def form_valid(self, form):
        project = Project(name=form.cleaned_data['name'], description=form.cleaned_data['description'], language=form.cleaned_data['language'], pub_date=form.cleaned_data['pub_date'], category=form.cleaned_data['category'], image=form.cleaned_data['image'])
        project.save()
        form.delete_temporary_files()
        return super(CreateProject, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateProject, self).get_context_data(**kwargs)
        context['title'] = _('Projects')
        return context   

#Edit list of Projects 
class ProjectsEditList(LoginRequiredMixin, ListView):
    model = Project 
    template_name = 'cgapp/editlist.html'
    login_url = '/dashboard/'
    def get_context_data(self, **kwargs):
        context = super(ProjectsEditList, self).get_context_data(**kwargs)
        context['edit_url'] = 'cgapp:edit-project'
        context['delete_url'] = 'cgapp:delete-project'
        context['title'] = _('Projects') 
        return context

#Delete Project page
class DeleteProject(LoginRequiredMixin, DeleteView):
    model = Project 
    template_name = 'cgapp/delete-project.html'
    success_url = '/dashboard/projects/list/'

#Edit Project Page
class DisplayProject(LoginRequiredMixin, DetailView):
    template_name = 'cgapp/edit.html'
    login_url = '/dashboard/'
    model = Project 
    def get_context_data(self, **kwargs):
        context = super(DisplayProject, self).get_context_data(**kwargs)
        context['form'] = ProjectForm()
        context['title'] = _('Projects') 
        return context

class UpdateProject(SuccessMessageMixin, SingleObjectMixin, FormView):
    form_class = ProjectForm 
    model = Project
    success_message = _("A project was updated successfully")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(UpdateProject, self).post(request, *args, **kwargs)
    
    def form_valid(self, form):
        #obtain current object 
        params = { 'pk': form.cleaned_data['object_id'] }
        project = Project.objects.get(**params)

        project.name=form.cleaned_data['name'] 
        project.category=form.cleaned_data['category'] 
        project.language=form.cleaned_data['language']
        project.pub_date=form.cleaned_data['pub_date']
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
class CreatePartner(SuccessMessageMixin, LoginRequiredMixin, FormView):
    form_class = PartnerForm 
    template_name = 'cgapp/create.html'
    success_url = '/dashboard/partner/add/'
    login_url = '/dashboard/'
    success_message = _("A partner was created successfully")
    def form_valid(self, form):
        partner = Partner(name=form.cleaned_data['name'], image=form.cleaned_data['image'])
        partner.save()
        form.delete_temporary_files()
        return super(CreatePartner, self).form_valid(form)
    def get_context_data(self, **kwargs):
        context = super(CreatePartner, self).get_context_data(**kwargs)
        context['title'] = _('Partners')
        return context


#Edit list of Partners 
class PartnersEditList(LoginRequiredMixin, ListView):
    model = Partner 
    template_name = 'cgapp/editlist.html'
    login_url = '/dashboard/'
    def get_context_data(self, **kwargs):
        context = super(PartnersEditList, self).get_context_data(**kwargs)
        context['edit_url'] = 'cgapp:edit-partner'
        context['delete_url'] = 'cgapp:delete-partner'
        context['title'] = _('Partners') 
        return context

#Delete Parnter page
class DeletePartner(DeleteView):
    model = Partner 
    success_url = '/dashboard/partners/list/'

#Edit Partner Page
class DisplayPartner(LoginRequiredMixin, DetailView):
    template_name = 'cgapp/edit.html'
    model = Partner 
    login_url = '/dashboard/'
    def get_context_data(self, **kwargs):
        context = super(DisplayPartner, self).get_context_data(**kwargs)
        context['form'] = PartnerForm()
        context['title'] = _('Partners') 
        return context

class UpdatePartner(SuccessMessageMixin, SingleObjectMixin, FormView):
    form_class = PartnerForm 
    model = Partner 
    success_message = _("A partner was updated successfully")

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

