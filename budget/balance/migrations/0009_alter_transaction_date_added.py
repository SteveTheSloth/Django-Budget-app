# Generated by Django 4.1.7 on 2023-02-22 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("balance", "0008_alter_transaction_date_added"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="date_added",
            field=models.DateField(auto_now_add=True),
        ),
    ]