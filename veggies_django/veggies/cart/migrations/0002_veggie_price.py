# Generated by Django 4.1.3 on 2022-11-25 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="veggie",
            name="price",
            field=models.IntegerField(default=0, max_length=11),
            preserve_default=False,
        ),
    ]