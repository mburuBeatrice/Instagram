from django import forms
from .models import Post,Profile

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['timestamp', 'lastupdated', 'likes', 'profile', 'comment']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo','bio']