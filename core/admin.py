from pyexpat import model
from django.contrib import admin
from .models import SignUp



@admin.register(SignUp)
class User(admin.ModelAdmin):
    list_display = ['id','user_type','locality','city','state','pin','profile_image']


# Register your models here.
