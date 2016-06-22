from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import CreateView

from main.models import Chrip, StopWord
# Create your views here.


class IndexView(ListView):
    template_name = "index.html"
    model = Chrip

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)     # if you want to extend your list view, must include this to keep functionality.
        context['ammount'] = Chrip.objects.all().count()
        return context

class ChirpDetailView(DetailView):
    model = Chrip

    def get_queryset(self):     # 90% of this use is for security
        return Chrip.objects.filter(bird=self.request.user)

class ChirpCreateView(CreateView):
    model = Chrip
    fields = ['body']
    success_url = '/'

    def form_valid(self, form):
        stop_words = StopWord.objects.all()
        # if trump clinton or sanders in body, add error
        chirp_data = form.cleaned_data['body'].lower()
        for stop_word in stop_words:
            if stop_word.word in chirp_data:
                form.add_error("body", "Can't we all get along")
                return self.form_invalid(form)

        # raise Exception(chirp_data) # test

        chirp = form.save(commit=False)
        chirp.bird = self.request.user
        return super().form_valid(form)
