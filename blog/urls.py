from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.post_list),
        url(r'^posts/$', views.posts, name='posts'),
        url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
        url(r'^contacto/$', views.contacto, name='contacto'),
        url(r'^post/new/$', views.post_new, name='post_new'),
        url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
        url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
        url(r'^tips/$', views.tips, name='tips'),
    ]