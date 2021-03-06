# Generated by Django 3.2.4 on 2021-08-25 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Historial', '0009_devices_historial_guia_devolucion'),
    ]

    operations = [
        migrations.AddField(
            model_name='devices_historial',
            name='correo_contacto',
            field=models.EmailField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='devices_historial',
            name='responsable',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
    ]
