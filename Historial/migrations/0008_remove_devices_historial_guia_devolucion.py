# Generated by Django 3.2.4 on 2021-08-16 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Historial', '0007_alter_devices_historial_guia_devolucion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devices_historial',
            name='guia_devolucion',
        ),
    ]