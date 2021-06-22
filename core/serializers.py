from .models import Product, Price, Store
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for the product model"""

    class Meta:
        model = Product
        fields = ('id', 'name',)


class PriceSerializer(serializers.ModelSerializer):
    """Serializer for prices"""
    product = ProductSerializer()

    class Meta:
        model = Price
        fields = (
            'product',
            'price',
        )


class StoreSerializer(serializers.ModelSerializer):
    """Serializer for the product model"""
    products = PriceSerializer(many=True, source='product_prices')

    class Meta:
        model = Store
        fields = ('name', 'address', 'products')
