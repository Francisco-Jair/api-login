# Generated by Django 4.0.5 on 2022-06-12 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='email',
            field=models.EmailField(error_messages={'unique': 'O email cadastrado já existe.'}, max_length=254, unique=True),
        ),
    ]
