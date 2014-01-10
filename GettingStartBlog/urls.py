from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GettingStartBlog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/$', 'blog.views.main'),
    url(r"^blog/(\d+)/$", 'blog.views.post'),
    url(r"^blog/add_comment/(\d+)/$", 'blog.views.add_comment'),
)
