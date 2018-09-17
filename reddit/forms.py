from django import forms
from reddit.models import *
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','password','email')

class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('title','content','user','picture','vote_total','site_url')