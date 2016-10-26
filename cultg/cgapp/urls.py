from django.conf.urls import url

from . import views

from django.contrib.auth import views as auth_views


app_name='cgapp'

urlpatterns = [
#Public pages
        url(r'^about/$', views.About.as_view(), name = 'about'),
        url(r'^$', views.Blog.as_view(), name = 'blog'),
        url(r'^post/(?P<pk>[0-9]+)/$', views.NewsPage.as_view(), name = 'news'),
        url(r'^team/$', views.Team.as_view(), name = 'team'),
        url(r'^projects/$', views.Projects.as_view(), name = 'projects'),
        url(r'^projects/(?P<pk>[0-9]+)/description/$', views.ProjectDetails.as_view(), name = 'project-page'),
        url(r'^team/member/(?P<pk>[0-9]+)/$', views.Members.as_view(), name = 'members'),
#Dashboard pages
        url(r'^dashboard/$', views.CreateNews.as_view(), name = 'create-news'),
        url('dashboard/members/add/$', views.CreateMember.as_view(), name = 'create-member'),
        url('dashboard/members/list/$', views.MemberEditList.as_view(), name = 'edit-member-list'),
        url('dashboard/members/edit/(?P<pk>[0-9]+)/$', views.EditMember.as_view(), name = 'edit-member'),
        url('dashboard/members/(?P<pk>[0-9]+)/delete$', views.DeleteMember.as_view(), name = 'delete-member'),
        url('dashboard/news/add/$', views.CreateNews.as_view(), name = 'create-news'),
        url('dashboard/news/list/$', views.NewsEditList.as_view(), name = 'edit-news-list'),
        url(r'^dashboard/news/edit/(?P<pk>\d+)/$', views.EditNews.as_view(), name='edit-news'),
        url(r'^dashboard/news/delete/(?P<pk>\d+)/$', views.DeleteNews.as_view(), name='delete-news'),
        url('dashboard/projects/add/$', views.CreateProject.as_view(), name = 'create-project'),
        url('dashboard/projects/list/$', views.ProjectsEditList.as_view(), name = 'edit-projects-list'),
        url(r'^dashboard/projects/edit/(?P<pk>\d+)/$', views.EditProject.as_view(), name='edit-project'),
        url(r'^dashboard/projects/delete/(?P<pk>\d+)/$', views.DeleteProject.as_view(), name='delete-project'),
        url('dashboard/partner/add/$', views.CreatePartner.as_view(), name = 'create-partner'),
        url('dashboard/partners/list/$', views.PartnersEditList.as_view(), name = 'edit-partners-list'),
        url(r'^dashboard/partners/edit/(?P<pk>\d+)/$', views.EditPartner.as_view(), name='edit-partner'),
        url(r'^dashboard/partners/delete/(?P<pk>\d+)/$', views.DeletePartner.as_view(), name='delete-partner'),

        ]
