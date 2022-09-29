# Generated by Django 4.1 on 2022-09-24 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_sucursal', models.IntegerField(verbose_name='Numero Sucursal')),
                ('nombre_sucursal', models.CharField(max_length=255, verbose_name='Nombre Sucursal')),
                ('direccion_sucursal', models.CharField(max_length=255, verbose_name='Direccion Sucursal')),
            ],
            options={
                'verbose_name': 'Sucursal',
                'verbose_name_plural': 'Sucursales',
                'db_table': 'Sucursal',
            },
        ),
    ]