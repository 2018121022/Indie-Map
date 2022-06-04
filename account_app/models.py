from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    STATUS_CHOICES = (
        (0, '관객'),
        (1, '뮤지션')
    )

    status = models.SmallIntegerField(choices = STATUS_CHOICES, default=0)
    name = models.CharField(max_length=200, default="익명")
    intro = models.TextField(null=True)
    insta = models.CharField(max_length=200, null=True)
    youtube = models.CharField(max_length=200, null=True)
    image = models.ImageField(blank = True, null = True)
    follower = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followers", blank=True)

class Concert(models.Model):
    musician = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    introduce = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    latitude = models.TextField()  # 위도
    longitude = models.TextField() # 경도
    address = models.TextField(null=True) # 주소
