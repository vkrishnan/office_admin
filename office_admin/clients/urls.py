from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.profile, name='profile'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', views.logout_page, name='logout'),
    url(r'^order/$', include("orders.urls", namespace='orders'))
]