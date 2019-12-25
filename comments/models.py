from django.db import models

# Create your models here.
class Comments(models.Model):
    name    =   models.CharField(max_length=30)
    email   =   models.EmailField()
    comment =   models.TextField(blank=False)
