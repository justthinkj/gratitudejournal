"""Defines URL patterns for learning_logs."""

from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    # Home page
    url(r'^$',views.index,name='index'),
    
    # Test: Info 
    url(r'^info$',views.info,name='info'),

    # Show all topics
    url(r'^topics/$',views.topics,name='topics'),

    # Detail page for a single topic
    url(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),

    # New topic
    url(r'new_topic/$',views.new_topic,name='new_topic'),

    # New entry
    url(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry,name='new_entry'),

    # Edit entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$',views.edit_entry,name='edit_entry'),
]