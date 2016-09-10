from django.conf.urls import url

from . import views

from django.contrib.auth import views as auth_views


app_name='cgapp'

urlpatterns = [
#Public pages
        url(r'^about/$', views.About.as_view(), name = 'about'),
        url(r'^$', views.NewsPage.as_view(), name = 'news'),
        url(r'^team/$', views.Team.as_view(), name = 'team'),
        url(r'^projects/$', views.Projects.as_view(), name = 'projects'),
        url(r'^projects/detail/$', views.ProjectDetail.as_view(), name = 'project-page'),
        url(r'^gallery/$', views.Gallery.as_view(), name = 'gallery'),
        url(r'^team/(?P<pk>[0-9]+)/$', views.Members.as_view(), name = 'members'),
#Dashboard pages
        url(r'^dashboard/$', views.CreateMember.as_view(), name = 'create-member'),
        url('dashboard/members/add$', views.CreateMember.as_view(), name = 'create-member'),
        url('dashboard/members/(?P<pk>[0-9]+)/$', views.EditMember.as_view(), name = 'edit-member'),
        url('dashboard/members/(?P<pk>[0-9]+)/delete$', views.DeleteMember.as_view(), name = 'delete-member'),
        url('dashboard/news/add/$', views.CreateNews.as_view(), name = 'create-news'),
        ]
