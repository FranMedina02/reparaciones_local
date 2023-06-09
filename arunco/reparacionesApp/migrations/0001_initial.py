# Generated by Django 4.2 on 2023-05-01 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('telefono', models.CharField(blank=True, max_length=13, null=True, unique=True)),
                ('mail', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('empresa', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Encargos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('encargado', models.BooleanField(default=False)),
                ('costo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ManoDeObra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horas', models.IntegerField(verbose_name='Horas estimadas')),
                ('orden', models.IntegerField()),
            ],
            options={
                'ordering': ['orden'],
            },
        ),
        migrations.CreateModel(
            name='Repuestos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('proveedor', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reparaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_entrada', models.DateField(auto_now_add=True)),
                ('fecha_salida', models.DateField(blank=True, null=True)),
                ('nombre', models.CharField(max_length=50)),
                ('total', models.IntegerField(blank=True, null=True, verbose_name='costo')),
                ('venta', models.IntegerField(blank=True, null=True)),
                ('confirmado', models.BooleanField(default=False)),
                ('plazo_de_entrega', models.DateField(blank=True, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reparacionesApp.clientes', verbose_name='Cliente')),
                ('repuestos', models.ManyToManyField(blank=True, null=True, through='reparacionesApp.Encargos', to='reparacionesApp.repuestos')),
                ('trabajo', models.ManyToManyField(through='reparacionesApp.ManoDeObra', to='reparacionesApp.trabajos')),
            ],
        ),
        migrations.AddField(
            model_name='manodeobra',
            name='reparacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reparacionesApp.reparaciones'),
        ),
        migrations.AddField(
            model_name='manodeobra',
            name='trabajo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reparacionesApp.trabajos', verbose_name='Trabajo realizado'),
        ),
        migrations.AddField(
            model_name='encargos',
            name='repuesto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reparacionesApp.repuestos', verbose_name='A comprar'),
        ),
        migrations.AddField(
            model_name='encargos',
            name='trabajo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reparacionesApp.reparaciones'),
        ),
    ]
