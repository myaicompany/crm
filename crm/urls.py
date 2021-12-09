from home.views import pageNotFound
from django.conf.urls import handler400
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

from a_crm.views import * 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('crm/', include('a_crm.urls')),
    path('per/', include('b_per.urls')),
    path('rpt/', include('c_rpt.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound