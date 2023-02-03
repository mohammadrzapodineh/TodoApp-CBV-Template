from django.http.response import Http404
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
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
        '''
        Show Todo lists In Todo Index Html With TodoCreateForm
        '''
        context['ojbect_list'] = Todo.objects.filter(user=self.request.user)
        return context


class EditTodoViwe(LoginRequiredMixin, UpdateView):
    model = Todo
    template_name = 'Todo/index.html'
    form_class = TodoCreateForm
    success_url = reverse_lazy('Todo:index_page')

    def get_object(self):
        '''
        Override For Get A Todo And Check Its Belong To Curent User Or not Return PermissionDeined
        '''
        todo = super().get_object()
        if todo.user == self.request.user:
            return super().get_object()
        raise PermissionDenied
class DeleteTodoView(LoginRequiredMixin, DeleteView):
    model = Todo
    template_name_suffix = '_delete'
    success_url = reverse_lazy('Todo:index_page')

    def get_object(self):
        '''
        Override For Get A Todo And Check Its Belong To Curent User Or not Return PermissionDeined
        '''
        todo = super().get_object()
        if todo.user == self.request.user:
            return super().get_object()
        raise PermissionDenied