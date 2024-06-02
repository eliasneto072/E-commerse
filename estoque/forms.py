from django import forms
from .models import Produto, Vendedor, Cliente, Compra

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


#


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['produto', 'cliente', 'vendedor']
        widgets = {
            'produto': forms.HiddenInput(),
        }



