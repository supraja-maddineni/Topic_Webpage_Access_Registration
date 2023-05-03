from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Topic(models.Model):
    topic_name=models.CharField(max_length=100)


class Webpage(models.Model):
    name=models.CharField(max_length=100)
    url=models.URLField()
    email=models.EmailField()


class AccessRecord(models.Model):
    author=models.CharField(max_length=100)
    date=models.DateField()