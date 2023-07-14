from django.urls import path
from .views import docente, docente_detalle, docente_listado, docente_crear

urlpatterns = [
    path('', docente),
    path('docente_listado/', docente_listado, name='docente_listado'),
    path('docente_crear/', docente_crear, name='docente_crear'),
    path('docente_detalle/<int:id>', docente_detalle, name="docente_detalle")
]


