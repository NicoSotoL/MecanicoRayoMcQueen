# Generated by Django 3.1.3 on 2023-06-24 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Taller', '0003_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]