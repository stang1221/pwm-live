# Generated by Django 4.2.16 on 2024-10-23 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0008_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="mfa_secret",
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
