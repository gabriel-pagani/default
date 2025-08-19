from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('login/done', views.login_done, name='login-done'),
    path('logout/', views.logout, name='logout'),
]
