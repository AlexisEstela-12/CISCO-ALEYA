# Generated by Django 3.2.4 on 2021-08-16 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Historial', '0004_devices_historial_codigo_prestamo'),
    ]

    operations = [
        migrations.AddField(
            model_name='devices_historial',
            name='guia_devolucion',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
