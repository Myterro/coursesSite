from django.urls import path
from django.contrib import admin
from django.urls import include
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from .views import login_redirect

urlpatterns = [
    path('', login_redirect, name='login_redirect'),
    path('courser/', include('courser.urls')),
    path('admin/', admin.site.urls)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
