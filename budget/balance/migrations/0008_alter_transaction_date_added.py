# Generated by Django 4.1.7 on 2023-02-22 11:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("balance", "0007_rename_telefone_transaction_telephone_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="date_added",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 2, 22, 11, 43, 1, 8819, tzinfo=datetime.timezone.utc
                ),
                editable=False,
            ),
        ),
    ]
