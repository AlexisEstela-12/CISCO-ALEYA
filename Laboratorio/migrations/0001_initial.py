# Generated by Django 3.2.4 on 2021-07-21 17:07

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
            name='Devices_Lab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.CharField(max_length=50)),
                ('serial_number', models.CharField(max_length=50, unique=True)),
                ('modelo', models.CharField(max_length=50)),
                ('ubicacion', models.CharField(max_length=30)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Laboratorio.estado_lab')),
            ],
            options={
                'verbose_name': 'Device',
                'verbose_name_plural': 'Devices',
            },
        ),
    ]
