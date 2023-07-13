# Generated by Django 4.2.3 on 2023-07-11 17:16

import Users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Users", "0002_alter_account_password"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="account",
            managers=[
                ("objects", Users.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name="account",
            name="last_login",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="last login"
            ),
        ),
    ]
