from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class TodoCreateView(CreateView):
    template_name = 'Todo/index.html'
    