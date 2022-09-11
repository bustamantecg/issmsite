from django.urls import path
from secretaria import views

urlpatterns = [
    path('', views.secretaria),
#  ------------------ path para Carreras ----------------------------------------------
    path('carreras_listado/', views.carreras_listado),
    path('carrera_listado/', views.carrera_listado, name='carrera_listado'),
    path('carreras_detalle/<int:id>', views.carreras_detalle),

#  ------------------ path para Alumnos ----------------------------------------------
    path('alumno_consulta/', views.alumno_consulta, name='alumno_consulta'),
    path('alumno_listado/', views.alumno_listado, name='alumno_listado'),
    path('buscar_alumno_dni/', views.buscar_alumno_dni, name='buscar_alumno_dni'),

#  ------------------ path para Docentes ----------------------------------------------
    path('docentes_listado/', views.docentes_listado, name='docentes_listado')
]