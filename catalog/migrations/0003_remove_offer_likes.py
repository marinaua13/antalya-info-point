# Generated by Django 5.0.3 on 2024-04-07 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_offer_likes"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="offer",
            name="likes",
        ),
    ]
