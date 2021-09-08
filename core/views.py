from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

from core.models import Evento


#
# def index(request):
#     return redirect('/admin/')
@csrf_exempt
def login_user(request):
    return render(request, 'login.html')


@csrf_exempt
def logout_user(request):
    logout(request)
    return redirect('/')


@csrf_exempt
@login_required(login_url='/login/')
def evento(request):
    return render(request, 'evento.html')


@csrf_exempt
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou Senha Inválidos")
    return redirect('/')


@csrf_exempt
@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        local = request.POST.get('local')
        descricao = request.POST.get('descricao')
        usuario = request.user
        Evento.objects.create(
            titulo=titulo,
            data_evento=data_evento,
            local=local,
            descricao=descricao,
            usuario=usuario
        )
    return redirect('/')

@csrf_exempt
def local_evento(request, titulo):
    consulta = Evento.objects.get(titulo=titulo)
    return HttpResponse(consulta.local)


@csrf_exempt
@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)
