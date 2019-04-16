from django.contrib import admin
from django.urls import path
from searcher.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('/search', search),
]
