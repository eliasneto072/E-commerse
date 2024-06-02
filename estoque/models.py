from django.db import models
from django.contrib.auth.models import User

class Vendedor(models.Model):
    nome = models.CharField(max_length=30, blank=True, null=True)
    telefone = models.CharField(max_length=12, blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    salario = models.DecimalField(max_digits=6, decimal_places=2, blank= True, null=True)

    def __str__(self):
        return self.nome



class Cliente(models.Model):
    nome = models.CharField(max_length=30, blank=True, null=True)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=40, unique=True, blank=True, null=True)
    telefone = models.CharField(max_length=12, blank=True, null=True)  

    def __str__(self):
        return self.nome
    



class Produto(models.Model):
    nome = models.CharField(max_length=30, blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    qtd = models.IntegerField(blank=True, null=True)
    img = models.ImageField(upload_to='produtos', blank=True, null=True)

    def subtrair_estoque(self, quantidade):
        self.qtd -= quantidade
        self.save()

    def __str__(self):
        return self.nome

class Compra(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.SET_NULL, blank=True, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, blank=True, null=True)
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, blank=True, null=True)
    data_compra = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'Produto : {self.produto} | Vendedor : {self.vendedor} | Cliente : {self.cliente} | Data : {self.data_compra}'



