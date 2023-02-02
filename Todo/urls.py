from django.urls import path
from .views import TodoCreateView

app_name = 'Todo'
urlpatterns = [
    path('', TodoCreateView.as_view(), name='index_page')
]