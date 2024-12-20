# Generated by Django 5.0.9 on 2024-11-25 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=150, unique=True)),
                ('cpf', models.CharField(blank=True, default='', max_length=14, null=True, unique=True)),
                ('rg', models.CharField(blank=True, max_length=12, null=True, unique=True)),
                ('cnpj', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('cro', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('datanasc', models.DateField(blank=True, null=True)),
                ('endereco', models.CharField(blank=True, max_length=100, null=True)),
                ('numero', models.CharField(blank=True, max_length=10, null=True)),
                ('complemento', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('bairro', models.CharField(blank=True, max_length=50, null=True)),
                ('cidade', models.CharField(blank=True, max_length=50, null=True)),
                ('uf', models.CharField(blank=True, max_length=2, null=True)),
                ('cep', models.CharField(blank=True, max_length=10, null=True)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('celular', models.CharField(blank=True, max_length=20, null=True)),
                ('whatsapp', models.BooleanField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('instagram', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
