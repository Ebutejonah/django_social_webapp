# Generated by Django 4.1.1 on 2023-03-31 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0042_alter_post_num_of_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='num_of_likes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
