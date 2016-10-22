from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView
import datetime

# Create your views here.


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


class Home(TemplateView):
    template_name = "dashboard/index.html"
