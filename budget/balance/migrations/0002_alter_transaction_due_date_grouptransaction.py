# Generated by Django 4.1.7 on 2023-03-06 15:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
        ("balance", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="due_date",
            field=models.DateField(default=datetime.date(2023, 3, 6)),
        ),
        migrations.CreateModel(
            name="GroupTransaction",
            fields=[
                (
                    "transaction_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="balance.transaction",
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="user.usergroup"
                    ),
                ),
            ],
            bases=("balance.transaction",),
        ),
    ]
