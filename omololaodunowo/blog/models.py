from django.db import models
from django.forms import CharField
from django.contrib.auth import get_user_model

# Create your models here.
class POST(models.Model):
    title=models.CharField(max_length=200)
    text=models.TextField()
    author=models.get_user_model()
    created_date=models.DateTimeField()
    published_date=models.DateTimeField()

