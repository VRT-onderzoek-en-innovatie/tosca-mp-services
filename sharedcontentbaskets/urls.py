from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from sharedcontentbaskets import views

urlpatterns = patterns('',
    url(r'^baskets/$', views.SharedContentBasketList.as_view()),
    url(r'^baskets/(?P<pk>[0-9]+)/$', views.SharedContentBasketDetail.as_view()),
    url(r'^baskets/(?P<pk>[0-9]+)/users/((?P<field_pk>[0-9]+)/)?$', views.SharedContentBasketUserList.as_view()),
    url(r'^baskets/(?P<pk>[0-9]+)/users/update/(?P<field_pk>[0-9]+)/?$', views.SharedContentBasketAddUser.as_view()),
    url(r'^baskets/(?P<pk>[0-9]+)/content/((?P<field_pk>[0-9]+)/)?$', views.SharedContentBasketContentList.as_view()),
    url(r'^baskets/(?P<pk>[0-9]+)/content/update/(?P<field_pk>[0-9]+)/?$', views.SharedContentBasketAddContent.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/baskets/$', views.UserContentBasketList.as_view()),
    url(r'^users/lookup/(?P<pk>[0-9a-zA-Z ]+)/$', views.UserLookup.as_view()),
    url(r'^content/$', views.ContentList.as_view()),
    url(r'^content/(?P<pk>[0-9]+)/$', views.ContentDetail.as_view()),
    url(r'^content/lookup/(?P<pk>[0-9a-zA-Z ]+)/$', views.ContentLookup.as_view()),
    url(r'^content/(?P<pk>[0-9]+)/baskets/$', views.ContentContentBasketList.as_view()),
)
