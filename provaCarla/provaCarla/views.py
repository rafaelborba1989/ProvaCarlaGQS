from django.shortcuts import render, get_object_or_404, redirect
from .models import Coleta, Criacao
from .forms import ColetaForm, CriacaoForm

def listar_coletas(request):
    coletas = Coleta.objects.all().order_by('-data')
    return render(request, 'listar_coletas.html', {'coletas': coletas})

def detalhes_coleta(request, coleta_id):
    coleta = get_object_or_404(Coleta, id=coleta_id)
    return render(request, 'detalhes_coleta.html', {'coleta': coleta})

def deletar_coleta(request, coleta_id):
    coleta = get_object_or_404(Coleta, id=coleta_id)
    if request.method == 'POST':
        coleta.delete()
        return redirect('listar_coletas')
    return render(request, 'confirmar_delecao.html', {'coleta': coleta})

def criar_coleta(request):
    if request.method == 'POST':
        form = ColetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_coletas')
    else:
        form = ColetaForm()
    return render(request, 'criar_coleta.html', {'form': form})

def criar_criacao(request):
    if request.method == 'POST':
        form = CriacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_coletas')
    else:
        form = CriacaoForm()
    return render(request, 'criar_criacao.html', {'form': form})
