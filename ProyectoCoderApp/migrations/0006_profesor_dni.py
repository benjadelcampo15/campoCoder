# Generated by Django 4.0.5 on 2022-06-24 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoCoderApp', '0005_alter_profesor_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='dni',
            field=models.IntegerField(default=321),
            preserve_default=False,
        ),
    ]
