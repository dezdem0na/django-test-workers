from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',
    url(r'^$', 'workers.views.index', name='index'),
    url(r'^([a-z]+)/$', 'workers.views.display', name='display'),
    url(r'^([a-z]+)/add/$', 'workers.views.add_new', name='add_new'),
    url(r'^([a-z]+)/ajax_update/$', 'workers.views.ajax_update', name='ajax_update'),
)