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
        url(r'^gallery/$', views.Gallery.as_view(), name = 'gallery'),
        url(r'^team/member/(?P<pk>[0-9]+)/$', views.Members.as_view(), name = 'members'),
#Dashboard pages
        url(r'^dashboard/$', views.CreateMember.as_view(), name = 'create-member'),
        url('dashboard/members/add$', views.CreateMember.as_view(), name = 'create-member'),
        url('dashboard/members/(?P<pk>[0-9]+)/$', views.EditMember.as_view(), name = 'edit-member'),
        url('dashboard/members/(?P<pk>[0-9]+)/delete$', views.DeleteMember.as_view(), name = 'delete-member'),
        url('dashboard/news/add/$', views.CreateNews.as_view(), name = 'create-news'),
        url('dashboard/projects/add/$', views.CreateProject.as_view(), name = 'create-project'),
        ]
