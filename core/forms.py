from django import forms
from .models import Post, Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pics','background_profile_pics','bio','country','city']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude =('id','user','likes','time_of_post',)