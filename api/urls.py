from django.conf.urls import url

from api import views

urlpatterns = [
    url(r'foreclosures/$', views.foreclosure_list),
    url(r'people/$', views.person_list),
    url(r'letters/$', views.create_letters),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]