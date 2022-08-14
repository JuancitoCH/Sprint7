# Generated by Django 4.0.6 on 2022-08-14 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarcasTarjeta',
            fields=[
                ('mt_id', models.AutoField(db_column='MT_id', primary_key=True, serialize=False)),
                ('mt_nombre', models.TextField(db_column='MT_nombre', unique=True)),
            ],
            options={
                'db_table': 'Marcas_Tarjeta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('numero', models.CharField(db_column='Numero', max_length=16, primary_key=True, serialize=False)),
                ('cvv', models.IntegerField(db_column='CVV')),
                ('f_otorgamiento', models.DateTimeField(db_column='F_Otorgamiento')),
                ('f_vencimiento', models.DateTimeField(db_column='F_Vencimiento')),
                ('fk_cliente', models.IntegerField()),
            ],
            options={
                'db_table': 'tarjeta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoTarjeta',
            fields=[
                ('tipo_tarjeta_id', models.AutoField(db_column='Tipo_tarjeta_id', primary_key=True, serialize=False)),
                ('tipo', models.TextField(db_column='Tipo', unique=True)),
            ],
            options={
                'db_table': 'Tipo_tarjeta',
                'managed': False,
            },
        ),
    ]