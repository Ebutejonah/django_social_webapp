from django import forms
from .models import Post, Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('id_user',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude =('id','user','likes','time_of_post',)