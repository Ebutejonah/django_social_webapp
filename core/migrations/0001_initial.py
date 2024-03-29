# Generated by Django 4.1.1 on 2023-08-03 14:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=200, null=True)),
                ('following', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LikePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(blank=True, max_length=200, null=True)),
                ('liked_by', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Searches',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=30, null=True)),
                ('name_first', models.CharField(max_length=50, null=True)),
                ('name_last', models.CharField(max_length=50, null=True)),
                ('id_user', models.IntegerField()),
                ('profile_pics', models.ImageField(blank=True, default='profile_pics/defaultimage2.jpg', null=True, upload_to='profile_pics')),
                ('background_profile_pics', models.ImageField(blank=True, default='bg_profile_pics/defaultimage.jpg', null=True, upload_to='bg_profile_pics')),
                ('country', models.CharField(blank=True, default='', max_length=40, null=True)),
                ('city', models.CharField(blank=True, default='', max_length=40, null=True)),
                ('bio', models.TextField(blank=True, default='', null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('followers', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='core.follow')),
                ('following', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.follow')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=100, null=True)),
                ('post_file', models.FileField(blank=True, null=True, upload_to='file_post')),
                ('caption', models.TextField(blank=True, null=True)),
                ('no_of_comments', models.IntegerField(blank=True, default=0, null=True)),
                ('time_of_post', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('num_of_likes', models.IntegerField(blank=True, default=0, null=True)),
                ('likes', models.ManyToManyField(blank=True, to='core.likepost')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.profile')),
            ],
        ),
        migrations.AddField(
            model_name='likepost',
            name='post_reference',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.post'),
        ),
        migrations.AddField(
            model_name='follow',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.profile'),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('time_of_comment', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('total_comments', models.IntegerField(blank=True, default=0, null=True)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.post')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.profile')),
            ],
            options={
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
