from django.urls import path, include

app_name = 'api-v1'
urlpatterns = [
    path('todo/', include('Todo.api.v1.urls'))
]