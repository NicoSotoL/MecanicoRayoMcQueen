# Generated by Django 3.1.3 on 2023-06-24 09:04

import TallerMecanico.Taller.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Taller', '0006_remove_publicacion_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='imagen',
            field=models.ImageField(default=2, upload_to=TallerMecanico.Taller.models.imagen),
            preserve_default=False,
        ),
    ]
