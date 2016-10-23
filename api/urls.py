from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'snippets/$', views.foreclosure_list),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]