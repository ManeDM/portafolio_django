# Generated by Django 4.1.7 on 2023-02-15 16:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("landing", "0002_alter_project_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.ImageField(upload_to="media/images"),
        ),
    ]