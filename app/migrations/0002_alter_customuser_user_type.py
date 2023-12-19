# Generated by Django 4.2.7 on 2023-12-19 10:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="user_type",
            field=models.CharField(
                choices=[("1", "HOD"), ("2", "STAFF"), ("3", "STUDENT")],
                default=1,
                max_length=50,
            ),
        ),
    ]
