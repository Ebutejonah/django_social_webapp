# Generated by Django 4.1.1 on 2023-03-30 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_alter_profile_continent_alter_profile_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='continent',
            new_name='city',
        ),
    ]