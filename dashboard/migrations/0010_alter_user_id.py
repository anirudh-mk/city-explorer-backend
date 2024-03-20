# Generated by Django 4.2.7 on 2024-03-20 11:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0009_alter_user_id_alter_user_last_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.CharField(
                default=uuid.UUID("28d52fc2-95cc-49a3-a160-cce119609f87"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
