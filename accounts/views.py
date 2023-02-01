from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import UserAuthenticationForm


class UserLoginView(LoginView):
    '''
    Login Users With A Custom Authentication Form
    '''
    template_name = 'accounts/login_page.html'
    redirect_authenticated_user = True
    authentication_form = UserAuthenticationForm