# Generated by Django 4.1.7 on 2023-03-09 10:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="myuser",
            old_name="active_group",
            new_name="group",
        ),
    ]
