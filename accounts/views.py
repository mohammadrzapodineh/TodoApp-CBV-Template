from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserLoginForm, UserRegisterForm
from django.views.generic import CreateView


class UserLoginView(LoginView):
    '''
    Login Users With A Custom Authentication Form
    '''
    template_name = 'accounts/login_page.html'
    redirect_authenticated_user = True
    form_class = UserLoginForm


class UserRegisterView(CreateView):
    template_name = 'accounts/register_page.html'
    form_class = UserRegisterForm 
    success_url = reverse_lazy('accounts:login_page')

    def get(self, request, *args, **kwargs):
        '''
        override Get Method For Check And Redirect Authenticated Users
        '''
        if request.user.is_authenticated:
            return redirect('Todo:index_page')
        return super().get(request, *args, **kwargs)

class UserLogOutView(LoginRequiredMixin, LogoutView):
    template_name = 'accounts/log-out_page.html'