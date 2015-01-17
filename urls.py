from django.conf.urls import patterns, url, include
from discuss import views

urlpatterns = patterns('',

    url(r'^$', views.home, name="home"),
    
    url(r'^subjects/(?P<pk>[0-9]+)/$', views.subject_detail, name="subject"),
    url(r'^subjects/$', views.SubjectListView.as_view(), name="subject"),
    url(r'^add-comment/$', views.add_comment, name="addcomment"),
    url(r'^login/$', views.login, name="login"),
    
    
)
