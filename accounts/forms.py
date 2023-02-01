from django import forms 
from django.contrib.auth.forms import AuthenticationForm
        

class UserAuthenticationForm(AuthenticationForm):
    '''
    Override Authentication Form For Our Custom Classes Style 
    and You Can Style Without Overrider With Django-tweaks !
    '''
    username = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control form-control-lg', 'id': 'typeEmailX'}))
    password = forms.CharField(max_length=110, widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-lg', 'id': 'typePasswordX'}))    


    def confirm_login_allowed(self, user):
        pass