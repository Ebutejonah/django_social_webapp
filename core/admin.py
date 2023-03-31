from django.contrib import admin
from .models import Profile, Post, Follow,LikePost, Comments

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Follow)
admin.site.register(LikePost)
admin.site.register(Comments)
