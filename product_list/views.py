from django.shortcuts import render
from .models import Product
from rest_framework import viewsets
from .serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductCustomFilter
# Create your views here.


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends= [DjangoFilterBackend]
    filterset_class = ProductCustomFilter