# cuentas/urls.py
from django.urls import path
from .views import VistaRegistro

urlpatterns = [
    path('registro/', VistaRegistro.as_view(), name='signup'),
]

#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