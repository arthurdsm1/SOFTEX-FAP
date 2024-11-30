import os
import django
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.db import models
from django import forms
from django.urls import path
from django.core.management import call_command

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meuprojeto.settings")
django.setup()

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.nome} - R${self.preco}"

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco']

def testar_modelo():
    produto = Produto.objects.create(nome="Cadeira", preco=199.99)
    return f"Produto criado: {produto}"

def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Produto criado com sucesso!")
    else:
        form = ProdutoForm()
    return render(request, 'criar_produto.html', {'form': form})

def testar_template(request):
    return render(request, 'teste_template.html', {'mensagem': 'Olá, Django!'})

def testar_urls():
    urls = [
        path('produto/', criar_produto),
        path('teste/', testar_template),
    ]
    return urls

def testar_migracoes():
    call_command('makemigrations')
    call_command('migrate')
    return "Migrações aplicadas com sucesso!"

def testar_servidor():
    from django.core.management.commands.runserver import Command
    command = Command()
    command.execute()

def main():
    print(testar_modelo())
    print(testar_migracoes()) 
    print("Testes concluídos.")

if __name__ == "__main__":
    main()
