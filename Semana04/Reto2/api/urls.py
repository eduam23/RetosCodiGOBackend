
from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.index),
    path('mascota',views.mascotas),
    path('mascota/<int:mascota_id>',views.mascotasedit),
    path('vacunas',views.vacunas),
    path('vacunas/<int:vacuna_id>',views.vacunasedit)
]