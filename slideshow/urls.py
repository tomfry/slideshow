from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'slideshow.slideshow_views.photos'),
    url(r'^photos/$', 'slideshow.slideshow_views.photos'),
    url(r'^photos/tn/(?P<album>[a-zA-Z0-9_-]+)/(?P<image>[a-zA-Z0-9_.-]+)$', 'slideshow.slideshow_views.renderThumbnail'),
    url(r'^photos/view/(?P<album>[a-zA-Z0-9_-]+)/$', 'slideshow.slideshow_views.album'),
)
