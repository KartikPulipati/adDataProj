from django.db import models
from rater.models import User
#from embed_video.fields import EmbedVideoField

MAX_NAME_LENGTH = 200
MAX_TITLE_LENGTH = 200

# Create your models here.
class Business(models.Model):
    name = models.CharField(max_length=MAX_NAME_LENGTH)

class Video(models.Model):

    file = models.FileField(upload_to='videos')
    #embedded = EmbedVideoField(blank=True)
    title = models.CharField(max_length=MAX_TITLE_LENGTH)
    uploader = models.ForeignKey(Business, on_delete=models.CASCADE)
    upload_date = models.DateField(auto_now_add=True)
    num_views = models.IntegerField()
    num_questions = models.IntegerField()
    reward_per_question = models.FloatField()

    def get_title(self):
        return self.title

class Tag(models.Model):
    category = models.CharField(max_length=MAX_TITLE_LENGTH)
    vids_by_category = models.ManyToManyField(Video)

