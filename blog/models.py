
from django.db import models
choice=(
    ('Mental Health','Mental Health'),
    ('Covid-19','Covid-19'),
    ('Heart Disease','Heart Disease'),
    ('Immune System','Immune System'),
)

class Post(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='postimg/')
    category=models.CharField(choices=choice,max_length=100)
    content=models.TextField(max_length=400)
    summary=models.CharField(max_length=300)

    
