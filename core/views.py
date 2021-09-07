from django.shortcuts import render, HttpResponse, redirect

from core.models import Evento

#
# def index(request):
#     return redirect('/admin/')

def local_evento(request, titulo):
    consulta = Evento.objects.get(titulo=titulo)
    return HttpResponse(consulta.local)


def lista_eventos(request):
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)
