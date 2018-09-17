from django.contrib import admin

# Register your models here.
from django.contrib import admin
from reddit.models import *
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Post)