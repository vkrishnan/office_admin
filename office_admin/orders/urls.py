from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.order_page, name='create_order'),
]