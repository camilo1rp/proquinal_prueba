# Generated by Django 3.2.4 on 2021-06-22 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_price_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='active',
            field=models.BooleanField(choices=[(True, 'Activo'), (False, 'Inactivo')], default=False, verbose_name='Activo'),
        ),
    ]