from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TodoCreateForm
from .models import Todo

class TodoCreateView(LoginRequiredMixin, CreateView):
    template_name = 'Todo/index.html'
    form_class = TodoCreateForm
    success_url = reverse_lazy('Todo:index_page')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    
    def get_context_data(self):
        context = super().get_context_data()
        context['ojbect_list'] = Todo.objects.filter(user=self.request.user)
        print(context['ojbect_list'])
        return context