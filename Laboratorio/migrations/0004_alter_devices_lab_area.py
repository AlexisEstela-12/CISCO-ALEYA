# Generated by Django 3.2.4 on 2021-07-27 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Laboratorio', '0003_devices_lab_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devices_lab',
            name='area',
            field=models.ForeignKey(default='Collaboration', on_delete=django.db.models.deletion.CASCADE, to='Laboratorio.sector'),
        ),
    ]
