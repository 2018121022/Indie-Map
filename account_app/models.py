from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
#from django.urls import reverse
#from django.utils.translation import ugettext_lazy as__


# Create your models here.

class User(AbstractUser):
    STATUS_CHOICES = (
        (0, '관객'),
        (1, '뮤지션')
    )

    status = models.SmallIntegerField(choices = STATUS_CHOICES, default=0)
    name = models.CharField(max_length=200, default="익명")
    intro = models.TextField(null=True)
    insta = models.URLField( null=True) #url 필드
    youtube = models.URLField( null=True) #url 필드
    image = models.ImageField(blank = True, null = True)
    follower = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followers", blank=True)

"""    
class UserHighlight(models.Model): #jian
    id = models.ForeignKey(User, on_delete=models.CASCADE) #외래키 참조
    photo = models.ImageField(default='media/highlight/default_image.jpeg', upload_to='highlight',
                              blank=True, null=True)
"""