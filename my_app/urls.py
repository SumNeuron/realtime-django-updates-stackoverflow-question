from django.conf.urls import url

from . import views


app_name = "my_app"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^query/(?P<query_id>[0-9]+)/$', views.query, name='query'),
]
