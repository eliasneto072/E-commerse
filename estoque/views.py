from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Vendedor, Cliente, Compra
from .forms import CompraForm, ClienteForm, VendedorForm, ProdutoForm

from decimal import Decimal

def produtos(request):
    produtos = Produto.objects.all()
    context = {'produtos' : produtos}
    return render(request, 'base.html', context)

def cadastrar_clientes(request):
    forms = ClienteForm()
    context = {'forms' : forms}
    return render(request, 'clienteForm.html', context)

def cliente(request):
    if request.method == 'POST': 
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)  # Salva o cliente, mas não comita ainda
            request.session['cliente_nome'] = cliente.nome  # Armazena o nome do cliente na sessão
            cliente.save()  # Agora sim, salva o cliente completamente
            return redirect('produtos')
    else:
        form = ClienteForm()
    return render(request, 'cliente.html', {'form': form})


def comprar(request, nome):
    produto = get_object_or_404(Produto, nome=nome)
    
    if request.method == 'POST':
        form = CompraForm(request.POST)
        quantidade_comprada = int(request.POST.get('quantidade_inpt', 0))

        if 0 < quantidade_comprada <= produto.qtd:
            if form.is_valid():
                vendedor_nome = form.cleaned_data['vendedor']
                vendedor = get_object_or_404(Vendedor, nome=vendedor_nome)

                compra = form.save(commit=False)
                compra.produto = produto
                compra.save()

                # Imposto
                imposto = produto.preco * Decimal(0.25)
                preco = produto.preco - imposto
                print(imposto)
                # Calculando o valor total da compra (5% do valor do produto)
                valor_compra = preco * Decimal(quantidade_comprada) * Decimal(0.05)

                # Adicionando o valor da compra ao salário do vendedor
                novo_salario = vendedor.salario + valor_compra
                vendedor.salario = novo_salario
                vendedor.save()

                produto.subtrair_estoque(quantidade_comprada)
                return redirect('produtos')
    else:
        form = CompraForm()

    context = {'produto': produto, 'forms': form}
    return render(request, 'compra.html', context)



def relatorio(request):
    compras = Compra.objects.all().order_by('-data_compra')
    total_imposto = Decimal(0)

    for compra in compras:
        imposto = compra.produto.preco * Decimal(0.25)
        total_imposto += imposto

    context = {'compras': compras, 'total_imposto': total_imposto}
    return render(request, 'relatorio.html', context)
