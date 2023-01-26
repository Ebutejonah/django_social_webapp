from django.contrib import admin
from .models import Profile, Post, Follow,LikePost, Continent, Country, Comments

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Follow)
admin.site.register(LikePost)
admin.site.register(Continent)
admin.site.register(Country)
admin.site.register(Comments)
