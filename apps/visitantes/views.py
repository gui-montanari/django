from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from visitantes.forms import VisitanteForm, AutorizaVisitanteForm
from visitantes.models import Visitante
from django.utils import timezone
from django.http import HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required

@login_required
def registrar_visitante(request):

    form = VisitanteForm()

    if request.method == "POST":
        form = VisitanteForm(request.POST)

        if form.is_valid():
            visitante = form.save(commit=False)

            visitante.registrado_por = request.user.porteiros # o porteiro que registrou o visitante é o usuário logado
            visitante.save() # salva o visitante no banco de dados

            messages.success(request, "Visitante registrado com sucesso!") # para adicionar uma mensagem de sucesso

            return redirect("index") # redireciona para a página inicial

    context = {
        "nome_pagina": "Registrar Visitante",
        "form": form
    }

    return render(request, "registrar_visitante.html", context)

@login_required
def informacoes_visitante(request, id): # recebe o id do visitante

    visitante = get_object_or_404( # pega o objeto do banco de dados
        Visitante, # modelo
        id=id # id do visitante
    )

    form = AutorizaVisitanteForm() # cria um formulário de autorização


    if request.method == "POST":
        form = AutorizaVisitanteForm(
            request.POST,
            instance=visitante
            )
        
        if form.is_valid():
            visitante = form.save(commit=False)

            visitante.status = "EM_VISITA" # muda o status do visitante para "EM_VISITA"
            visitante.hora_autorizacao = timezone.now()
            visitante.save() # salva o visitante no banco de dados

            messages.success(request, "Visitante autorizado com sucesso!") # mensagem de sucesso
        return redirect("index")

    context = {
        "nome_pagina": "Informações do Visitante", # nome da página
        "visitante": visitante, # objeto visitante
        "form": form # formulário
    }

    return render(request, "informacoes_visitante.html", context) # renderiza a página

@login_required
def finalizar_visita(request, id): # recebe o id do visitante

    if request.method == "POST":
        visitante = get_object_or_404(
            Visitante, 
            id=id)
        visitante.status = "FINALIZADO"
        visitante.horario_saida = timezone.now()
        visitante.save()

        messages.success(request, "Visita finalizada com sucesso!") # mensagem de sucesso
        return redirect("index")
    
    else:
        return HttpResponseNotAllowed(
            ["POST"],
            "Método não permitido"
            )