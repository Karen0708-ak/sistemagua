# Generated by Django 5.2 on 2025-05-22 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('cedula', models.CharField(max_length=20, unique=True)),
                ('especialidad', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
    ]
