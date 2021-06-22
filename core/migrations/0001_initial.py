# Generated by Django 3.2.4 on 2021-06-22 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, verbose_name='Nombre del producto')),
            ],
            options={
                'verbose_name': 'Producto',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, verbose_name='Nombre de la tienda')),
                ('address', models.CharField(max_length=255, verbose_name='Dirección')),
                ('active', models.BooleanField(default=False, verbose_name='Activo')),
                ('products', models.ManyToManyField(related_name='stores', through='core.Price', to='core.Product')),
            ],
            options={
                'verbose_name': 'tienda',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='price',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_prices', to='core.product'),
        ),
        migrations.AddField(
            model_name='price',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_prices', to='core.store'),
        ),
    ]