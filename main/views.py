from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from main.models import Chrip, StopWord, Profile
# Create your views here.


class IndexView(CreateView):
    template_name = "index.html"
    model = Chrip
    fields = ['body']
    success_url = reverse_lazy('index_view')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)     # if you want to extend your list view, must include this to keep functionality.
        context['ammount'] = Chrip.objects.all().count()
        context['object_list'] = Chrip.objects.all()
        return context

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

class ChirpDetailView(DetailView):
    model = Chrip

    def get_queryset(self):     # 90% of this use is for security
        return Chrip.objects.filter(bird=self.request.user)
        

class ProfileUpdateView(UpdateView):
    fields = ['fav_bird']
    success_url = reverse_lazy('profile_update_view')

    # overides the need for a pk in url
    def get_object(self, query_set=None):
        return self.request.user.profile

class ChirpDeleteView(DeleteView):
    success_url = reverse_lazy('index_view')

    def get_queryset(self):
        return Chrip.objects.filter(bird=self.request.user)
