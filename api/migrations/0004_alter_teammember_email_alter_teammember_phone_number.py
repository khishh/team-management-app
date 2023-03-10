# Generated by Django 4.1.6 on 2023-02-10 06:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_rename_role_teammember_is_admin"),
    ]

    operations = [
        migrations.AlterField(
            model_name="teammember",
            name="email",
            field=models.EmailField(
                max_length=255,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[A-Za-z0-9_!#$%&'*+\\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$",
                        message="Invalid Email format",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="teammember",
            name="phone_number",
            field=models.CharField(
                max_length=12,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[0-9]{3}-[0-9]{3}-[0-9]{4}",
                        message="Phone number has to be 123-456-7890 format",
                    )
                ],
            ),
        ),
    ]
