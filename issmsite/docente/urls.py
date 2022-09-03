from django.urls import path
from . import views
from .views import docentes

urlpatterns = [
    path('', docentes),
]