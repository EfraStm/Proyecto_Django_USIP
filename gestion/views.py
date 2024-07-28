#from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Categoria, Producto, Cliente, Pedido
from .serializers import CategoriaSerializer, ProductoSerializer, ClienteSerializer, PedidoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class CustomAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"message": "Esta es una Custom API"})