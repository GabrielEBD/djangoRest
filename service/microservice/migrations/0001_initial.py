# Generated by Django 2.2.6 on 2019-10-06 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedido_id', models.IntegerField()),
                ('costo_total', models.IntegerField()),
                ('impuesto_IVA', models.IntegerField()),
            ],
        ),
    ]
