# Generated by Django 4.2 on 2023-05-01 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reparacionesApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reparaciones',
            name='repuestos',
            field=models.ManyToManyField(blank=True, through='reparacionesApp.Encargos', to='reparacionesApp.repuestos'),
        ),
    ]