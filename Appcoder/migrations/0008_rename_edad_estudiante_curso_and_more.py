# Generated by Django 4.1.1 on 2022-10-11 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appcoder', '0007_rename_alumno_estudiante'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudiante',
            old_name='Edad',
            new_name='curso',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='Profesion',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='apellido',
        ),
        migrations.AddField(
            model_name='estudiante',
            name='camada',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
