# Generated by Django 4.0.5 on 2022-07-18 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoCoderApp', '0008_alter_avatar_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posteo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('cuerpo', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
                ('foto', models.ImageField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
    ]
