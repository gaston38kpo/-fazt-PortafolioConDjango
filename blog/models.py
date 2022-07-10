from datetime import date
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images/')
    date = models.DateField(default=date.today)
