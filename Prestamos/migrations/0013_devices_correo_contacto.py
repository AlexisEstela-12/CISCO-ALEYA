# Generated by Django 3.2.4 on 2021-08-18 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prestamos', '0012_alter_devices_guia'),
    ]

    operations = [
        migrations.AddField(
            model_name='devices',
            name='correo_contacto',
            field=models.EmailField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]