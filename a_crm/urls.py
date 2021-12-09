from django.conf.urls import url
from django.urls import path

from .views import *


urlpatterns = [
    
    path('test/<str:bla>/', test, name='test'),

    # path('lst', Lst.as_view(), name='lst'),

    # path('itm/<int:itm_id>/che', Che.as_view(), name='che'),
    path('itm/<int:itm_id>/che', che, name='che'),
    
    # path('itm/<int:itm_id>/remfile', remfile, name='remfile'),


    # path('', Home.as_view(), name='home'),
    
    path('lst', Lst.as_view(), name='lst'),
    # path('lst', lst, name='lst'),

    path('itm/<int:itm_id>', Itm.as_view(), name='itm'),
    path('itm/<int:itm_id>/rem', Rem.as_view(), name='rem'),

    path('itm/add', Add.as_view(), name='add'),
    
    path('invoice/<int:itm_id>', invoice, name='invoice'),


    
    # path('inf/', InfLst.as_view(), name='inflst'),
    # path('inf/<int:inf_id>', InfOne.as_view(), name='infone'),




    # path('lgn', Lgn.as_view(), name='lgn'),
    # path('rgt', Rgt.as_view(), name='rgt'),
    # path('per', Per.as_view(), name='per'),
    # path('lgt', lgt, name='lgt'),

]