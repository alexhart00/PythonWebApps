from distutils.log import Log
from re import template
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Investigator



class InvestigatorListView(ListView):
    template_name = 'investigator/list.html'
    model = Investigator

class InvestigatorDetailView(DetailView):
    template_name = 'investigator/detail.html'
    model = Investigator


class InvestigatorCreateView(LoginRequiredMixin, CreateView):
    template_name = "investigator/add.html"
    model = Investigator
    fields = '__all__'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    success_url = reverse_lazy('investigator_list')



class InvestigatorUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "investigator/edit.html"
    model = Investigator
    fields = '__all__'
    success_url = reverse_lazy('investigator_list')


class InvestigatorDeleteView(LoginRequiredMixin,DeleteView):
    model = Investigator
    template_name = 'investigator/delete.html'
    success_url = reverse_lazy('investigator_list')

