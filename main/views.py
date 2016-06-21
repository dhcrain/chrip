from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from main.models import Chrip
# Create your views here.


class IndexView(ListView):
    template_name = "index.html"
    model = Chrip

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)     # if you want to extend your list view, must include this to keep functionality.
        context['ammount'] = Chrip.objects.all().count()
        return context
