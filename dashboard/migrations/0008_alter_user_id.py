# Generated by Django 4.2.7 on 2024-03-20 10:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0007_user_is_staff_user_is_superuser_user_last_login_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.CharField(
                default=uuid.UUID("864b8d91-7b7f-4e26-8920-3346c1beac67"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
