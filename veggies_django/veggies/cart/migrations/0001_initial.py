# Generated by Django 4.1.3 on 2022-11-25 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Veggie",
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
                ("category", models.CharField(max_length=2000)),
                ("image", models.CharField(max_length=10000)),
                ("name", models.CharField(max_length=2000)),
            ],
            options={"db_table": "veggie",},
        ),
    ]
