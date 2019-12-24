from django.db import models

# Create your models here.
class Blog(models.Model):
    title       =   models.CharField(max_length=60)
    author      =   models.CharField(max_length=30, null=True)
    date        =   models.DateTimeField(auto_now=False, auto_now_add=True)
    summary     =   models.TextField(blank=True, null=True)
    description =   models.TextField(blank=False, null=True)
    image       =   models.ImageField(upload_to='posts/', blank=False, null=True)
    