import os
import django
from django.conf import settings
from django.db import models
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django import forms
from django.urls import path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meuprojeto.settings")
django.setup()

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    descricao = models.TextField()

    def __str__(self):
        return f"{self.nome} - R${self.preco}"

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'descricao']

def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Produto criado com sucesso!")
    else:
        form = ProdutoForm()
    return render(request, 'criar_produto.html', {'form': form})

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'listar_produtos.html', {'produtos': produtos})

def registrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registrar_usuario.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Credenciais inválidas")
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('produto/criar/', criar_produto, name='criar_produto'),
    path('produtos/', listar_produtos, name='listar_produtos'),
    path('registrar/', registrar_usuario, name='registrar_usuario'),
    path('login/', login_usuario, name='login'),
    path('', home, name='home'),
]

if __name__ == "__main__":
    from django.core.management import call_command
    call_command('makemigrations')
    call_command('migrate')
    call_command('runserver')
