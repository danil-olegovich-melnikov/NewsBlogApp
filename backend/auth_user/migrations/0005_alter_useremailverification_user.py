# Generated by Django 3.2 on 2022-01-19 03:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth_user', '0004_auto_20220117_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useremailverification',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username', verbose_name='Пользователь'),
        ),
    ]