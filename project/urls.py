from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('_shortener.urls', namespace='shortener')),
    path('', include('auth.urls', namespace='auth')),
]
