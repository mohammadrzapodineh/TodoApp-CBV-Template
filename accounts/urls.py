from django.urls import path
from .views import UserLoginView, UserRegisterView, UserLogOutView


app_name = 'accounts'
urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login_page'),
    path('register/', UserRegisterView.as_view(), name='register_page'),
    path('log-out', UserLogOutView.as_view(), name='log-out')
]