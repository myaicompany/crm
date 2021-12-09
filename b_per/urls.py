from django.conf.urls import url
from django.urls import path

from .views import *


urlpatterns = [
    # path('', Per.as_view(), name='per'),
    path('', per, name='per'),
]