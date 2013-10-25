from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'melbdjango.views.home', name='home'),
    url(r'^posts/', include('posts.urls')),
    url(r'^hacks/', include('hacks.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'django.shortcuts.render', {'template_name': 'index.html'}),
)
