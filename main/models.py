from django.db import models

# Create your models here.


class Chrip(models.Model):
    body = models.CharField(max_length = 141)
    created = models.DateTimeField(auto_now_add=True)
    bird = models.ForeignKey("auth.User")

    class Meta:
        ordering = ['-created']


class StopWord(models.Model):
    word = models.CharField(max_length=26)

class 
