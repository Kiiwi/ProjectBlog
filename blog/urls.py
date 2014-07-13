from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

from blogapp.feed import LatestEntriesFeed


admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^about/', 'blogapp.views.about'),
                       url(r'^feed/$', LatestEntriesFeed()),
                       url(r'^$', 'blogapp.views.index'),
                       url(r'^(?P<slug>[\w\-]+)/$', 'blogapp.views.post'),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

