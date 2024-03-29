# Generated by Django 4.1.3 on 2023-01-01 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppTurnos1', '0013_remove_turnos_dia_remove_turnos_obrasocial_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turnos',
            name='hora',
        ),
        migrations.AlterField(
            model_name='medicos',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppTurnos1.especialidades'),
        ),
        migrations.CreateModel(
            name='agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desde', models.DateTimeField(blank=True, null=True, verbose_name='Dia / Desde hora')),
                ('hasta', models.TimeField(blank=True, null=True, verbose_name='Hasta hora')),
                ('medico', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='AppTurnos1.medicos')),
            ],
        ),
        migrations.AlterField(
            model_name='turnos',
            name='agenda',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='AppTurnos1.agenda'),
        ),
        migrations.DeleteModel(
            name='agendas',
        ),
    ]
