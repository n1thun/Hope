from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView
import datetime
from api.models import Person
from vanilla import CreateView, DeleteView, ListView, UpdateView




# Create your views here.


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


class Home(TemplateView):
    template_name = "dashboard/index.html"

class Success(TemplateView):
    template_name = "dashboard/success.html"

class Register(CreateView):
    model = Person
    fields = '__all__'
    template_name = "dashboard/register.html"

    success_url = '/success/'


class Org(TemplateView):
    template_name = "dashboard/org.html"
