# Generated by Django 4.1.3 on 2022-12-31 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppTurnos1', '0009_rename_dedicacion_medicos_servicio'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='agenda',
            new_name='agendas',
        ),
        migrations.RenameField(
            model_name='pacientes',
            old_name='fechaNacimento',
            new_name='fecha_Nacimento',
        ),
    ]
