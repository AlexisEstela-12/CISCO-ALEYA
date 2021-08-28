# Generated by Django 3.2.4 on 2021-07-27 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Laboratorio', '0002_sector'),
    ]

    operations = [
        migrations.AddField(
            model_name='devices_lab',
            name='area',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='Laboratorio.sector'),
            preserve_default=False,
        ),
    ]
