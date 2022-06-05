from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone
from allauth.socialaccount.models import SocialAccount

# Create your models here.

class User(AbstractUser):
    STATUS_CHOICES = (
        (0, '관객'),
        (1, '뮤지션')
    )

    ALARM_CHOICES = (
        (0, 'OFF'),
        (1, 'ON')
    )

    status = models.SmallIntegerField(choices = STATUS_CHOICES, default=0)
    alarm = models.SmallIntegerField(choices = ALARM_CHOICES, default=1)
    name = models.CharField(max_length=200, default="익명")
    intro = models.TextField(null=True)
    insta = models.URLField( null=True) #url 필드
    youtube = models.URLField( null=True) #url 필드
    image = models.ImageField(blank = True, null = True)
    follower = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followers", blank=True)


class Concert(models.Model):
    musician = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    introduce = models.TextField(null=True)
    date = models.DateField()
    time = models.TimeField()
    latitude = models.TextField()  # 위도
    longitude = models.TextField() # 경도
    address = models.TextField(null=True) # 주소

    def __str__(self):
        return self.introduce

class Feedback(models.Model):
    feedback_post = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    feedback_name = models.CharField(max_length=200, default="익명")
    feedback_profile = models.ImageField(blank = True, null = True)
    feedback_content = models.CharField(max_length=200)
    feedback_image = models.ImageField(blank = True, null = True)
    feedback_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.feedback_content

class Highlight(models.Model):
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    highlight = models.ImageField(blank = True, null = True)
    highlight_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.uploader.name