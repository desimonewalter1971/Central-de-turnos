# Generated by Django 4.1.3 on 2022-12-30 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppTurnos1', '0008_turnos_delete_turno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicos',
            old_name='dedicacion',
            new_name='servicio',
        ),
    ]
