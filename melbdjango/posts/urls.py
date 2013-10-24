from django.conf.urls import patterns, url
from .views import PostsView

urlpatterns = patterns('',
    url(r'^$', PostsView.as_view()),
)
