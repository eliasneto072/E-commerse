import django_filters
from .models import Compra

class CompraFilter(django_filters.FilterSet):
    class Meta:
        model = Compra
        fields = {
            'vendedor__nome' : ['icontains'],
            'cliente__nome' : ['icontains'],
            'produto__nome' : ['icontains'],
            'data_compra' : ['exact'],
        }