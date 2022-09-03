from django.urls import path

from .views import alumnos, mesas_listado, alumno_perfil

urlpatterns = [
    path('', alumnos),
    path('mesas_listado/', mesas_listado),
    path('alumno_perfil/', alumno_perfil),
]