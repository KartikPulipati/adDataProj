from django.db import models
from rater.models import User

MAX_NAME_LENGTH = 200
MAX_TITLE_LENGTH = 200

# Create your models here.
class Business(models.Model):
    name = models.CharField(max_length=MAX_NAME_LENGTH)

class Video(models.Model):
    file = models.FileField(upload_to='videos')
    title = models.CharField(max_length=MAX_TITLE_LENGTH)
    uploader = models.ForeignKey(Business, on_delete=models.CASCADE)
    upload_date = models.DateField(auto_now_add=True)
    num_views = models.IntegerField()

