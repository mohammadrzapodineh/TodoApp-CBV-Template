from django.urls import path
from .views import TodoCreateView, EditTodoViwe, DeleteTodoView

app_name = 'Todo'
urlpatterns = [
    path('', TodoCreateView.as_view(), name='index_page'),
    path('edit/<int:pk>/', EditTodoViwe.as_view(), name='edit_todo'),
    path('delete/<int:pk>/', DeleteTodoView.as_view(), name='delete_todo')
]