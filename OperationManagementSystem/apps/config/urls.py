# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = 'config'

urlpatterns = [
    url(r'^configfile/$', views.ConfigfileListView.as_view(), name='configfile'),
    url(r'^config_change/(?P<pk>[0-9]+)/$', views.ConfigChangeDetailView.as_view(), name='config_change'),
    url(r'^config_change_save/(?P<configfile_id>[0-9]+)/$', views.configfile_change_save, name='config_change_save'),
]
