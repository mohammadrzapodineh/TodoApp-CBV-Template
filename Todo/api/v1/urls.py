from django.urls import path
from .views import todo_list, todo_detail

app_name = 'Todo-Api'
urlpatterns = [
    path('list/', todo_list, name='todo_list'),
    path('detail/<int:pk>/', todo_detail, name='todo_detail')
]