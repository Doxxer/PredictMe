from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'Web.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^$', 'PredictMe.views.index', name='index'),
                       url(r'^search/(?P<query>.*)$', 'PredictMe.views.search', name='search'),
                       url(r'^admin/', include(admin.site.urls)),
)
