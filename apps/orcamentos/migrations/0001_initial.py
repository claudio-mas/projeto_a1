# Generated by Django 5.0.9 on 2024-11-26 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItensOrcamento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantidade', models.IntegerField()),
                ('valorunitario', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('desconto', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('valortotal', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('observacao', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Item do Orçamento',
                'verbose_name_plural': '3.2- Itens do Orçamento',
            },
        ),
        migrations.CreateModel(
            name='Orcamento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.CharField(blank=True, default='-', max_length=10, null=True)),
                ('data', models.DateField(blank=True, null=True)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('validade', models.DateField(blank=True, null=True)),
                ('status', models.CharField(default='Em Andamento', max_length=20)),
                ('pedido', models.CharField(blank=True, default='-', max_length=10, null=True)),
                ('datapedido', models.DateField(blank=True, null=True)),
                ('contrato', models.CharField(blank=True, default='-', max_length=10, null=True)),
                ('datacontrato', models.DateField(blank=True, null=True)),
                ('observacao', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Orçamento',
                'verbose_name_plural': '3.1- Orçamentos',
            },
        ),
    ]
