# Generated by Django 3.2.4 on 2021-08-13 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Historial', '0003_auto_20210809_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='devices_historial',
            name='codigo_prestamo',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
