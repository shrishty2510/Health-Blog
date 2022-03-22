from django.contrib import admin
from .models import Post

@admin.register(Post)
class UserModeladmin(admin.ModelAdmin):
    list_display = ['id','category','title','image','content','summary']


# Register your models here.
