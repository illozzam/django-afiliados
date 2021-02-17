from django.db import models
import requests

class Pagina(models.Model):
    url = models.CharField(max_length=200, unique=True)
    link_afiliado = models.CharField(max_length=255)
    link_pagina_venda = models.CharField(max_length=255)
    codigo = models.TextField(null=True, blank=True)
    acessos = models.IntegerField(default=0)

    def __str__(self):
        return self.url

class Acesso(models.Model):
    pagina = models.ForeignKey(Pagina, on_delete=models.CASCADE)
    ip = models.CharField(max_length=30, null=True, blank=True)
    dados_ip = models.TextField(null=True, blank=True)
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(
            self.data_hora.isoformat(),
            pagina.url
        )
