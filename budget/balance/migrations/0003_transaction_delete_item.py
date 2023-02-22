# Generated by Django 4.1.7 on 2023-02-22 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("balance", "0002_alter_item_due_date_alter_item_email_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transaction",
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
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Income", "Income"),
                            ("Expense", "Expense"),
                            ("Loan", "Loan"),
                        ],
                        default="Expense",
                        max_length=10,
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("purpose", models.CharField(max_length=200)),
                ("amount", models.FloatField(max_length=6)),
                ("due_date", models.DateField(null=True)),
                (
                    "repeat_pattern",
                    models.CharField(
                        choices=[
                            ("one off", "one off"),
                            ("monthly", "monthly"),
                            ("weekly", "weekly"),
                            ("every two weeks", "every two weeks"),
                            ("every three weeks", "every three weeks"),
                            ("every four weeks", "every four weeks"),
                        ],
                        default="monthly",
                        max_length=30,
                        null=True,
                    ),
                ),
                ("website", models.URLField(null=True)),
                ("email", models.EmailField(max_length=254, null=True)),
                ("telefone", models.PositiveBigIntegerField(null=True)),
                ("end_date", models.DateField(null=True)),
                ("date_added", models.DateField(default="22/02/2023", editable=False)),
            ],
        ),
        migrations.DeleteModel(
            name="Item",
        ),
    ]