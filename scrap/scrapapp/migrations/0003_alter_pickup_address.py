# Generated by Django 4.1 on 2023-07-02 08:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("scrapapp", "0002_pickup"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pickup",
            name="address",
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
