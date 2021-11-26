from django.db import models
from owner.models import Video

MAX_NAME_LENGTH = 200

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=MAX_NAME_LENGTH)
    liked_videos = models.ManyToManyField(Video)
    disliked_videos = models.ManyToManyField(Video)
    unrated_videos = models.ManyToManyField(Video)




