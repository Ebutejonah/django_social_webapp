from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name_first = models.CharField(max_length=50,null=True)
    name_last = models.CharField(max_length=50,null=True)
    id_user = models.IntegerField()
    profile_pics=models.ImageField(upload_to='profile_pics',default="profile_pics/defaultimage.jpg")
    background_profile_pics=models.ImageField(upload_to='bg_profile_pics',default="bg_profile_pics/defaultimage.jpg")
    continent = models.ForeignKey('Continent', on_delete=models.SET_NULL,  blank = False, null = True)
    country = models.ForeignKey('Country', on_delete=models.SET_NULL,  blank = False, null = True)
    bio = models.TextField(blank = True, null = True,default="")
    followers = models.ForeignKey('Follow', on_delete=models.SET_NULL,blank=True,null=True,related_name='followers')
    following = models.ForeignKey('Follow', on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100,null=True)
    post_file = models.FileField(upload_to='file_post',blank=True,null=True)
    caption = models.TextField(blank=True,null=True)
    likes = models.IntegerField(default=0,blank=True,null=True)
    no_of_comments = models.IntegerField(default=0,blank=True,null=True)
    time_of_post = models.DateTimeField(default = datetime.now,blank=True,null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.user + "'s post"


class Comments(models.Model):
    author = models.CharField(max_length=100,blank=True,null=True)
    comments = models.TextField(blank= True, null= True)
    total_comments = models.IntegerField(default = 0,blank = True, null= True)
    post = models.ForeignKey(Post, on_delete = models.CASCADE,null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null = True, blank = True)

    class  Meta:
        verbose_name_plural = 'Comments'


class Follow(models.Model):
    user = models.CharField(max_length=200,blank=True,null=True)
    following = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.user + " following @" + self.following


class LikePost(models.Model):
    post_id=models.CharField(max_length=200)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Continent(models.Model):
    name = models.CharField(max_length=100,null=True)
    continent = models.CharField(max_length=50)

    def __str__(self):
        return self.continent


class Country(models.Model):
    name = models.CharField(max_length=100,null=True)
    country = models.CharField(max_length=50)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.country


class Search(models.Model):
    name = models.CharField(max_length = 250)

    class Meta:
        verbose_name_plural = 'Searches'

    def __str__(self):
        return self.name