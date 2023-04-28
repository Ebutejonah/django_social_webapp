from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime



User = get_user_model()


class Profile(models.Model):
    username = models.CharField(blank=True,null=True,max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name_first = models.CharField(max_length=50,null=True)
    name_last = models.CharField(max_length=50,null=True)
    id_user = models.IntegerField()
    profile_pics=models.ImageField(null=True,blank=True,upload_to='profile_pics', default = 'profile_pics/defaultimage2.jpg')
    background_profile_pics=models.ImageField(null=True,blank=True,upload_to='bg_profile_pics', default = 'bg_profile_pics/defaultimage.jpg')
    country = models.CharField(max_length=40,null=True,blank=True,default="")
    city = models.CharField(max_length=40,null=True,blank=True,default="")
    bio = models.TextField(blank = True, null = True,default="")
    followers = models.ForeignKey('Follow', on_delete=models.CASCADE,blank=True,null=True,related_name='followers')
    following = models.ForeignKey('Follow', on_delete=models.CASCADE,blank=True,null=True)
    email = models.EmailField(null=True,blank=True)
    def __str__(self):
        return self.user.username
    

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100,null=True)
    post_file = models.FileField(upload_to='file_post',blank=True,null=True)
    caption = models.TextField(blank=True,null=True)
    likes = models.ManyToManyField('LikePost', blank=True)
    no_of_comments = models.IntegerField(default=0,blank=True,null=True)
    time_of_post = models.DateTimeField(default = datetime.now,blank=True,null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    num_of_likes = models.IntegerField(default=0,null=True,blank=True)

    def __str__(self):
        return self.user + "'s post"

class Comments(models.Model):
    author = models.CharField(max_length=100,blank=True,null=True)
    comments = models.TextField(blank= True, null= True)
    time_of_comment = models.DateTimeField(default=datetime.now, blank=True, null = True)
    total_comments = models.IntegerField(default = 0,blank = True, null= True)
    post = models.ForeignKey(Post, on_delete = models.CASCADE,null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null = True, blank = True)

    class  Meta:
        verbose_name_plural = 'Comments'


class Follow(models.Model):
    user = models.CharField(max_length=200,blank=True,null=True)
    following = models.CharField(max_length=200,blank=True,null=True)
    user_profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.user + " following @" + self.following


class LikePost(models.Model):
    post_id=models.CharField(max_length=200, null=True, blank=True)
    liked_by = models.CharField(max_length=100)
    post_reference = models.ForeignKey(Post, on_delete=models.CASCADE, null = True, blank= True)

    def __str__(self):
        return self.liked_by + " liked " + self.post_reference.user + "'s post"


class Search(models.Model):
    name = models.CharField(max_length = 250)

    class Meta:
        verbose_name_plural = 'Searches'

    def __str__(self):
        return self.name