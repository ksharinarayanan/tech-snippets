from django.db import models

from blog.models import Blog
# Create your models here.
class BlogContent(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()