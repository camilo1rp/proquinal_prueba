from django.contrib import admin

from .models import Store, Product, Price


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'active', ]


class PriceInline(admin.StackedInline):
    model = Price
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'tiendas', ]
    inlines = [PriceInline]

    def tiendas(self, obj):
        """list stores to show in admin"""
        return ",\n".join([a.name for a in obj.stores.all()])
