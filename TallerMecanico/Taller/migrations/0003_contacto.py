# Generated by Django 3.1.3 on 2023-06-22 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Taller', '0002_auto_20230621_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('idContacto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=255)),
                ('mensaje', models.TextField()),
            ],
        ),
    ]
