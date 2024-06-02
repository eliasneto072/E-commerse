from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.produtos, name='produtos'),
    path('cadastrar/clientes/', views.cadastrar_clientes, name='clienteForms'),
    path('cliente/', views.cliente, name='cliente'),
    path('comprar/<str:nome>/', views.comprar , name='comprar'),
    path('relatorio/', views.relatorio,  name='relatorio')

    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)