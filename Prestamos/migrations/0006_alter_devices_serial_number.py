# Generated by Django 3.2.4 on 2021-08-06 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prestamos', '0005_auto_20210806_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devices',
            name='serial_number',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]