# Generated by Django 4.1.3 on 2022-12-13 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTurnos1', '0002_alter_agendadisponiblepormedico_desde_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agendadisponiblepormedico',
            name='dia',
        ),
        migrations.AlterField(
            model_name='agendadisponiblepormedico',
            name='desde',
            field=models.DateTimeField(blank=True, null=True, verbose_name='dia/desde hora'),
        ),
        migrations.AlterField(
            model_name='agendadisponiblepormedico',
            name='hasta',
            field=models.TimeField(blank=True, null=True, verbose_name='hora hast'),
        ),
    ]
