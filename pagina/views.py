from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Pagina, Acesso
import requests

class MostraPaginaView(View):
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def get_data_by_ip(self, ip):
        api = 'a0fb9bb6270983be98f44de82db1383c008cb9db639b7887b13cc5b212e2373c'

        pesquisa = requests.get('http://api.ipinfodb.com/v3/ip-city/?key={}&ip={}'.format(
            api,
            ip
        ))

        return pesquisa.text if pesquisa.ok else None

    def get(self, request, **kwargs):
        pagina = Pagina.objects.get(url=kwargs['url_pagina'])

        #Atualiza o contador de acessos
        pagina.acessos += 1
        pagina.save()

        #Registra o acesso
        Acesso.objects.create(
            pagina=pagina,
            ip=self.get_client_ip(request),
            dados_ip=self.get_data_by_ip(self.get_client_ip(request))
        )

        if pagina.codigo:
            return render(request, 'pagina/base.html', {'pagina': pagina})
        else:
            return redirect(pagina.link_pagina_venda)
