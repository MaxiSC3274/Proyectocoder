# Generated by Django 4.1.1 on 2022-10-11 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appcoder', '0008_rename_edad_estudiante_curso_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='camada',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='curso',
        ),
    ]
