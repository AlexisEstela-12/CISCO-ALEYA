# Generated by Django 3.2.4 on 2021-08-26 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='estado_lab',
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
            name='sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sec', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'sector',
                'verbose_name_plural': 'sectores',
            },
        ),
        migrations.CreateModel(
            name='Devices_Lab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.CharField(max_length=50)),
                ('serial_number', models.CharField(max_length=50, unique=True)),
                ('modelo', models.CharField(max_length=50)),
                ('ubicacion', models.CharField(max_length=30)),
                ('area', models.ForeignKey(default='Collaboration', on_delete=django.db.models.deletion.CASCADE, to='Laboratorio_Costa_Rica.sector')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Laboratorio_Costa_Rica.estado_lab')),
            ],
            options={
                'verbose_name': 'Device',
                'verbose_name_plural': 'Devices',
            },
        ),
    ]
