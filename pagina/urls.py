from django.urls import path
from .views import MostraPaginaView

urlpatterns = [
    path('site/<str:url_pagina>/', MostraPaginaView.as_view(), name='mostra-pagina'),
]
