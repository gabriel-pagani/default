from django.urls import path
from . import views

app_name = 'shortener'

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug>/', views.redirect_link, name='redirect-link'),
]
