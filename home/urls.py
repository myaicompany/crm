from django.conf.urls import url
from django.urls import path

from .views import *


urlpatterns = [

    path('', Home.as_view(), name='home'),

    path('inf/', InfLst.as_view(), name='inflst'),
    path('inf/<int:inf_id>', InfOne.as_view(), name='infone'),

    path('lgn', Lgn.as_view(), name='lgn'),
    path('rgt', Rgt.as_view(), name='rgt'),
    path('lgt', lgt, name='lgt'),
    
    path('aboutcodes', aboutcodes, name='aboutcodes'),

]