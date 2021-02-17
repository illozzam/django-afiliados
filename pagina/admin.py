from django.contrib import admin
from .models import Pagina, Acesso

@admin.register(Pagina)
class PaginaAdmin(admin.ModelAdmin):
    list_display = ['url', 'link_pagina_venda', 'link_afiliado', 'acessos']

@admin.register(Acesso)
class AcessoAdmin(admin.ModelAdmin):
    list_display = ['data_hora', 'pagina', 'ip', 'dados_ip']
    ordering = ['data_hora']
    list_filter = ['data_hora']
