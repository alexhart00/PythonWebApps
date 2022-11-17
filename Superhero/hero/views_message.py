from distutils.log import Log
from re import template
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Message



class MessageListView(ListView):
    template_name = 'message/list.html'
    model = Message

class MessageDetailView(DetailView):
    template_name = 'message/detail.html'
    model = Message


class MessageCreateView(CreateView):
    template_name = "message/add.html"
    model = Message
    fields = '__all__'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    success_url = reverse_lazy('message_list')

class MessageUpdateView(UpdateView):
    template_name = "message/edit.html"
    model = Message
    fields = '__all__'
    success_url = reverse_lazy('message_list')


class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'message/delete.html'
    success_url = reverse_lazy('message_list')
