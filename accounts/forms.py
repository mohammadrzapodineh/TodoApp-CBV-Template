from django import forms 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()
# class UserLoginForm(forms.Form):
#     username = forms.EmailField(widget=forms.EmailInput(
#         attrs={'class': 'form-control form-control-lg', 'id': 'typeEmailX'}))
#     password = forms.CharField(max_length=110, widget=forms.PasswordInput(
#         attrs={'class': 'form-control form-control-lg', 'id': ' typePasswordX'}))    


class UserLoginForm(AuthenticationForm):
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


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')
        