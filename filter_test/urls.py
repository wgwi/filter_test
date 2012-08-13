from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from filter_test import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    # url(r'^$', 'filter_test.views.home', name='home'),
    # url(r'^filter_test/', include('filter_test.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^query/', 'project.views.product_list'),
    url(r'^query1/', 'project.views.product_t'),
    url(r'^admin/', include(admin.site.urls)),
)
