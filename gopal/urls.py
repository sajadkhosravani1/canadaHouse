from django.contrib import admin
from django.urls import path, include
from gopal.views import *

urlpatterns = [
    path('',home),
    path('list', list),
    path('estimate',estimate),
    path('R<int:house_id>', house_view)
]
