# Generated by Django 5.0.6 on 2024-07-07 15:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("agua", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TabelaAgua",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100, verbose_name="Nome")),
                (
                    "arsenio_total",
                    models.FloatField(
                        null=True, verbose_name="Arsênio total - mg/L As"
                    ),
                ),
                ("ordem", models.IntegerField()),
            ],
            options={
                "verbose_name": "Tabela de Água",
                "verbose_name_plural": "Tabelas de Água",
            },
        ),
    ]
