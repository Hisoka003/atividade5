# Generated by Django 5.1.3 on 2024-11-30 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_social', models.CharField(max_length=100)),
                ('nome_fantasia', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=18, unique=True)),
                ('telefone', models.CharField(max_length=20)),
                ('endereco', models.TextField()),
            ],
        ),
    ]
