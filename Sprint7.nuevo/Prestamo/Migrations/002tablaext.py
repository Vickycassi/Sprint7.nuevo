

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Prestamo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prestamo',
            options={'verbose_name': 'Prestamo', 'verbose_name_plural': 'Prestamos'},
        ),
        migrations.AlterModelTable(
            name='prestamo',
            table='Prestamo',
        ),
    ]