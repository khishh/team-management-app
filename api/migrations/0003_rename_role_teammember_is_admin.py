# Generated by Django 4.1.6 on 2023-02-08 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_teammember_role"),
    ]

    operations = [
        migrations.RenameField(
            model_name="teammember",
            old_name="role",
            new_name="is_admin",
        ),
    ]
