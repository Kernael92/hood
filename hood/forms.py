from .models import Post,Profile,Business,Hood,Comment
from django import forms
from django.forms import ModelForm,Textarea, IntegerField

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image','description','hood']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic','bio','email','hood']

class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'image','description','hood','email']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
