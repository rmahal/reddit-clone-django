from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100,blank=True)
    content = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    picture = models.ImageField(upload_to='post_pics', blank = True)
    vote_total = models.PositiveSmallIntegerField()
    site_url = models.URLField(blank=True)

    def __str__(self):
        return self.title