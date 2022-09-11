from django.urls import path, include

from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='Home'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('secretaria/', include('secretaria.urls')),
    path('alumno/', include('alumno.urls')),
    path('docente/', include('docente.urls')),
    path('contacto/', include('contacto.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)