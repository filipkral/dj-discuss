from django.conf.urls import patterns, url, include
from discuss import views

urlpatterns = patterns('',

    url(r'^$', views.home, name="home"),
    
    url(r'^subjects/(?P<pk>[0-9]+)/$', views.subject_detail, name="subject"),
    url(r'^subjects/$', views.SubjectListView.as_view(), name="subject"),
    url(r'^add-comment/$', views.add_comment, name="addcomment"),
    url(r'^login/$', views.login_page, name="login"),
    url(r'^login-user/$', views.login_user, name="login-user"),
    #url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="logout")
    url(r'^logout/$', 'views.logout_user', name="logout")
    
)
