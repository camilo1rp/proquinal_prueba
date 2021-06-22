from django.db import models


class Store(models.Model):
    """Model for store"""
    name = models.CharField(max_length=127, verbose_name="Nombre de la tienda")
    address = models.CharField(max_length=255, verbose_name="Dirección")
    active = models.BooleanField(default=False, verbose_name="Activo")
    products = models.ManyToManyField('Product',
                                      through='price',
                                      related_name='stores')

    class Meta:
        verbose_name = "tienda"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    """Model for products"""
    name = models.CharField(max_length=127, verbose_name="Nombre del producto")

    class Meta:
        verbose_name = "Producto"

    def __str__(self):
        return self.name


class Price(models.Model):
    """Intermediate table for prices"""
    store = models.ForeignKey('Store',
                              related_name="product_prices",
                              on_delete=models.CASCADE)
    product = models.ForeignKey('Product',
                               related_name='product_prices',
                               on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        unique_together = ('store', 'product')

    def __str__(self):
        return f'Precio de {self.product} para la tienda' \
               f' {self.store}: {self.price}'
