from django.urls import path, include

from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404
from homeapp.views import Error404View

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('store/', views.store, name='store'),

    path('secretaria/', include('secretaria.urls')),
    path('alumno/', include('alumno.urls')),
    path('docente/', include('docente.urls')),
    path('contacto/', include('contacto.urls')),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = Error404View.as_view()