# Generated by Django 4.2.7 on 2024-03-20 10:28

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0002_remove_user_last_login_remove_user_qr_code_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.CharField(
                default=uuid.UUID("6c8553e7-fdd6-4e5c-ad2b-68afd643b4d4"),
                max_length=36,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
