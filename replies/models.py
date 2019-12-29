from django.db import models

from comments.models import Comments

class Replies(models.Model):
    name            =   models.CharField(max_length=60)
    email           =   models.EmailField()
    reply           =   models.TextField()
    dateTime        =   models.DateTimeField(auto_now_add=True)
    baseComment     =   models.ForeignKey(Comments, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Replies"