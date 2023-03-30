# Generated by Django 4.1.7 on 2023-03-14 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("age", models.IntegerField(default=18)),
                ("name", models.CharField(default="Lucas", max_length=100)),
                ("gender", models.CharField(default="M", max_length=1)),
                (
                    "height",
                    models.DecimalField(decimal_places=2, default=1.7, max_digits=3),
                ),
            ],
        ),
    ]
