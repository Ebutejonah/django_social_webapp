# Generated by Django 4.1.1 on 2023-03-30 22:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0037_rename_continent_profile_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='continent',
        ),
        migrations.AddField(
            model_name='follow',
            name='user_object',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Continent',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]