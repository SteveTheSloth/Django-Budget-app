# Generated by Django 4.1.7 on 2023-02-22 11:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("balance", "0006_alter_transaction_date_added"),
    ]

    operations = [
        migrations.RenameField(
            model_name="transaction",
            old_name="telefone",
            new_name="telephone",
        ),
        migrations.AlterField(
            model_name="transaction",
            name="date_added",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 2, 22, 11, 26, 28, 4296, tzinfo=datetime.timezone.utc
                ),
                editable=False,
            ),
        ),
    ]
