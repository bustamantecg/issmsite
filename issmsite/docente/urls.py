from django.urls import path
from . import views
from .views import docente

urlpatterns = [
    path('', docente),
]