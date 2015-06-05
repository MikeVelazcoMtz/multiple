from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.usuarios.views import *
from django.conf import settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'multiple.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^[a-z0-9]{3,14}/list/user', UserListView.as_view(), name="user_list"),
    url(r'^clientes/list', ClienteListView.as_view(), name="clientes_list"),
    url(r'^clientes$', ClienteListView.as_view(), name="clientes_list"),
    url(r'^clientes/new', ClienteCreateView.as_view(), name="clientes_new"),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('', (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                            'document_root': settings.MEDIA_ROOT}))
