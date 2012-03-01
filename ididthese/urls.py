from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from cvs.views import index
from django.conf import settings

import logging

admin.autodiscover()
#logging.debug(settings.MEDIA_ROOT)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ididthese.views.home', name='home'),
    # url(r'^ididthese/', include('ididthese.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
)
if settings.DEBUG:
    
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',  
         {'document_root': settings.MEDIA_ROOT}),
    )