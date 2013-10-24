
from django.conf.urls import patterns, include, url

urlpatterns = patterns('hacks.views',
    url(r'^$', 'idea_list', name='idea-list'),
    url(r'^add/$', 'idea_add', name='idea-create'),
    url(r'^(?P<idea_id>\d+)/$', 'idea_detail', name='idea-detail'),
    url(r'^(?P<idea_id>\d+)/up/$', 'idea_vote', {'direction': 1}, name='idea-vote-up'),
    url(r'^(?P<idea_id>\d+)/down/$', 'idea_vote', {'direction': -1}, name='idea-vote-down'),
    url(r'^(?P<idea_id>\d+)/comment/$', 'idea_comment', name='idea-comment'),
)

