from django.db import models

from blog.models import Blog
# Create your models here.
class Comments(models.Model):
    name            =   models.CharField(max_length=60)
    email           =   models.EmailField(null=True, blank=True)
    comment         =   models.TextField()
    dateTime        =   models.DateTimeField(auto_now_add=True)
    blog            =   models.ForeignKey(Blog, on_delete=models.CASCADE, blank=True, null=True, default=None)
    parent          =   models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, default=None)

    class Meta:
        verbose_name_plural = "Comments"