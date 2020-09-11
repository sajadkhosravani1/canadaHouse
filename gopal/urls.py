from django.contrib import admin
from django.urls import path, include
from gopal.views import *

app_name = 'gopal'

urlpatterns = [
    path('', home, name='home'),
    path('list', list, name='list'),
    path('estimate', estimate, name='estimate'),
    path('R<int:house_id>', house_view, name='house_view')
]
