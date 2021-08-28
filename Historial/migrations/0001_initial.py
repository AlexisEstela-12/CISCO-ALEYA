# Generated by Django 3.2.4 on 2021-08-09 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devices_Historial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.CharField(max_length=50)),
                ('serial_number', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('AM', models.CharField(max_length=50)),
                ('partner', models.CharField(max_length=50)),
                ('cliente', models.CharField(max_length=50)),
                ('contacto', models.CharField(max_length=30)),
                ('Fprestamo', models.DateTimeField()),
                ('Fentregado', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Device',
                'verbose_name_plural': 'Devices',
            },
        ),
    ]
