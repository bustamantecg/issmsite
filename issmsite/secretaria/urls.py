from django.urls import path
from secretaria import views

urlpatterns = [
    path('', views.secretaria),
    path('alumnos_listado/', views.alumnos_lisatdo),
    path('carreras_listado/', views.carreras_listado),
    path('carreras_detalle/<int:id>', views.carreras_detalle),
]