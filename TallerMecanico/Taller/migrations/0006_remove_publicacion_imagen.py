# Generated by Django 3.1.3 on 2023-06-24 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Taller', '0005_auto_20230624_0454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicacion',
            name='imagen',
        ),
    ]