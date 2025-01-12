# Generated by Django 4.2 on 2023-04-17 14:25

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
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
                ("title", models.CharField(max_length=100)),
                ("content", models.TextField()),
                ("publish", models.BooleanField(default=True)),
                ("image", models.ImageField(upload_to="images/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("category", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Portfolio",
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
                ("title", models.CharField(max_length=100)),
                ("content", models.TextField()),
                ("image", models.ImageField(upload_to="images/")),
                ("category", models.CharField(max_length=50)),
            ],
        ),
    ]
