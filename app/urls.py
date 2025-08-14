from django.urls import path
from app.views import ferias, data_ferias


app_name = 'app'

urlpatterns = [
    path('', ferias, name='ferias'),
    path('api/data-ferias/', data_ferias, name='data-ferias'),
]
