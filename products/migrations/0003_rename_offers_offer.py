# Generated by Django 5.0.1 on 2024-01-25 22:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_offers"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Offers",
            new_name="Offer",
        ),
    ]
