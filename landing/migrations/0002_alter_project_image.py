# Generated by Django 4.1.7 on 2023-02-15 16:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("landing", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.ImageField(upload_to="images"),
        ),
    ]