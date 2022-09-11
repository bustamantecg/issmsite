from django.urls import path

from .views import alumnos, mesas_listado, alumno_perfil, mesas_detalles

urlpatterns = [
    path('', alumnos),
    path('mesas_listado/', mesas_listado),
    path('mesas_detalles/<int:id>', mesas_detalles),
    path('alumno_perfil/', alumno_perfil),
]