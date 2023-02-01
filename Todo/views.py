from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexPage(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
