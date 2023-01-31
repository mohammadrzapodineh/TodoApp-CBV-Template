from django.urls import path
from .views import IndexPage

app_name = 'Todo'
urlpatterns = [
    path('', IndexPage.as_view(), name='index_page')
]