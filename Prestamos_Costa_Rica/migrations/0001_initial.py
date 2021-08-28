# Generated by Django 3.2.4 on 2021-08-26 19:34

import Prestamos.cambiar_nombre_prestamo
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('telf', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Acount Manager',
                'verbose_name_plural': 'Acount Managers',
            },
        ),
        migrations.CreateModel(
            name='estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'state',
                'verbose_name_plural': 'states',
            },
        ),
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.CharField(max_length=50)),
                ('serial_number', models.CharField(max_length=50, unique=True)),
                ('modelo', models.CharField(max_length=50)),
                ('partner', models.CharField(max_length=50)),
                ('responsable', models.CharField(max_length=25)),
                ('cliente', models.CharField(max_length=50)),
                ('contacto', models.CharField(max_length=30)),
                ('correo_contacto', models.EmailField(max_length=40)),
                ('Fprestamo', models.DateTimeField()),
                ('Fentrega', models.DateTimeField()),
                ('guia', models.ImageField(blank=True, null=True, upload_to=Prestamos.cambiar_nombre_prestamo.path_and_rename)),
                ('codigo_prestamo', models.IntegerField()),
                ('AM', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Prestamos_Costa_Rica.am')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Prestamos_Costa_Rica.estado')),
            ],
            options={
                'verbose_name': 'Device',
                'verbose_name_plural': 'Devices',
            },
        ),
    ]
