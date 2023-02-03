
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import IdexTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('Todo.urls')),
    path('accounts/', include('accounts.urls')),
    path('', IdexTemplateView.as_view(), name='home_page')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)