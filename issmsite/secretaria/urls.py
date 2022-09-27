from django.contrib.auth.decorators import login_required
from django.urls import path

from secretaria.views import secretaria, carrera_listado, carreras_detalle, alumno_consulta, alumno_listado, \
    buscar_alumno_dni, docente_listado, alumno_inscribir_carrera, personas_listado, docente_crear, empleado_listado

urlpatterns = [
    path('', secretaria, name= 'inicio'),
#  ------------------ path para Carreras ----------------------------------------------
    path('carrera_listado/', carrera_listado, name='carrera_listado'),
    path('carreras_detalle/<int:id>', carreras_detalle),

#  ------------------ path para Alumnos ----------------------------------------------
    path('alumno_listado/', alumno_listado, name='alumno_listado'),
    path('alumno_inscribir_carrera/', alumno_inscribir_carrera, name='alumno_inscribir_carrera'),

    path('buscar_alumno_dni/', buscar_alumno_dni, name='buscar_alumno_dni'),
    path('alumno_consulta/', alumno_consulta, name='alumno_consulta'),

#  ------------------ path para Docentes ----------------------------------------------
    path('docente_listado/', docente_listado, name='docente_listado'),
    path('docente_crear/', docente_crear, name='docente_crear'),
    path('docente_editar/', docente_crear, name='docente_editar'),

#  ------------------ path para Personal de la Institucion ----------------------------
    path('empleado_listado/', empleado_listado, name='empleado_listado'),


#  ------------------ path para Personas ----------------------------------------------
    path('personas_listado/', personas_listado, name='personas_listado')

]