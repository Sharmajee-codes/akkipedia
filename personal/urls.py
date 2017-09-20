from django.conf.urls import url, include
from . import views
from blog import views as blog_views


urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^blog/',include("blog.urls", namespace="blog")),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
]
