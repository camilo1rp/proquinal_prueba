from .models import Product, Store
from .serializers import ProductSerializer, StoreSerializer
from rest_framework import generics


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    model = serializer_class.Meta.model


class StoreList(generics.ListAPIView):
    queryset = Store.objects.filter(active=True)
    serializer_class = StoreSerializer