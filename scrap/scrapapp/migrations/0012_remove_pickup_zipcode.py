# Generated by Django 4.1 on 2023-07-02 18:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("scrapapp", "0011_remove_pickup_pincode_pickup_zipcode"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pickup",
            name="zipcode",
        ),
    ]
