from django.db import models

from blog.models import Blog
# Create your models here.
class Comments(models.Model):
    name            =   models.CharField(max_length=60)
    email           =   models.EmailField()
    comment         =   models.TextField()
    dateTime        =   models.DateTimeField(auto_now_add=True)
    blog            =   models.ForeignKey(Blog, on_delete=models.CASCADE, default=None)

    class Meta:
        verbose_name_plural = "Comments"