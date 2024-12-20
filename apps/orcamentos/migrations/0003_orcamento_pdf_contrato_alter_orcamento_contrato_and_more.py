# Generated by Django 5.0.9 on 2024-11-26 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orcamentos', '0002_alter_orcamento_numero_alter_orcamento_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orcamento',
            name='pdf_contrato',
            field=models.FileField(blank=True, null=True, upload_to='orcamentos/', verbose_name='PDF Contrato'),
        ),
        migrations.AlterField(
            model_name='orcamento',
            name='contrato',
            field=models.CharField(blank=True, default='-', max_length=10, null=True, verbose_name='Nº Contrato'),
        ),
        migrations.AlterField(
            model_name='orcamento',
            name='data',
            field=models.DateField(blank=True, null=True, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='orcamento',
            name='datacontrato',
            field=models.DateField(blank=True, null=True, verbose_name='Data do Contrato'),
        ),
        migrations.AlterField(
            model_name='orcamento',
            name='datapedido',
            field=models.DateField(blank=True, null=True, verbose_name='Data do Pedido'),
        ),
        migrations.AlterField(
            model_name='orcamento',
            name='numero',
            field=models.CharField(max_length=10, verbose_name='Nº Orçamento'),
        ),
        migrations.AlterField(
            model_name='orcamento',
            name='observacao',
            field=models.TextField(blank=True, null=True, verbose_name='Observações'),
        ),
        migrations.AlterField(
            model_name='orcamento',
            name='pedido',
            field=models.CharField(blank=True, default='-', max_length=10, null=True, verbose_name='Nº Pedido'),
        ),
        migrations.AlterField(
            model_name='orcamento',
            name='status',
            field=models.CharField(blank=True, choices=[('Em Andamento', 'Em Andamento'), ('Aprovado', 'Aprovado'), ('Reprovado', 'Reprovado'), ('Cancelado', 'Cancelado')], default='Em Andamento', max_length=20, null=True, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='orcamento',
            name='validade',
            field=models.DateField(blank=True, null=True, verbose_name='Validade'),
        ),
        migrations.AlterField(
            model_name='orcamento',
            name='valor',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Valor'),
        ),
    ]
