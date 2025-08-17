from django.urls import path
from . import views

app_name = 'shortener'

urlpatterns = [
    path('', views.create_link, name='create_link'),
    path('<slug:slug>/', views.redirect_link, name='redirect_link'),
]
