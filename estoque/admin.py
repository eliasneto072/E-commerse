from django.contrib import admin
from .models import Vendedor, Cliente, Produto, Compra

admin.site.register(Produto)

admin.site.register(Vendedor)

admin.site.register(Cliente)

admin.site.register(Compra)
