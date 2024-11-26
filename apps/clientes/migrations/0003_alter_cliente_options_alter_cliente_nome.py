# Generated by Django 5.0.9 on 2024-11-25 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_alter_cliente_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name': 'Cliente', 'verbose_name_plural': 'Cadastro'},
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(help_text='Nome completo do cliente ou Razão Social', max_length=150, unique=True, verbose_name='Nome'),
        ),
    ]
