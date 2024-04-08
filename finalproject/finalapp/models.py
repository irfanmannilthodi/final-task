from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Marvel(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    img=models.ImageField(upload_to="marvel")
    year=models.DateField()
    cast=models.TextField()
    category=models.CharField(max_length=250)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    url=models.URLField()
    # review=models.TextField(null=True,blank=True)

class Dccomics(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    img=models.ImageField(upload_to="dccomics")
    year=models.DateField()
    cast=models.TextField()
    category=models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()d

    # review = models.TextField(null=True,blank=True)


class Monster(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    img=models.ImageField(upload_to="monster")
    year=models.DateField()
    cast=models.TextField()
    category=models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()
    # review = models.TextField(null=True,blank=True)



