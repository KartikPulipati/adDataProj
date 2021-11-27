from django.db import models
from rater.models import rater

MAX_TITLE_LENGTH = 200

class Advertisement(models.Model):
    title = models.CharField(max_length=MAX_TITLE_LENGTH)
    media_file = models.FileField(upload_to='media/')
    uploader = models.OneToOneField(Business)
    upload_date = models.DateField(auto_add_now=True)
    reward_per_question = models.FloatField()
    viewers = models.ManyToManyField(rater)
    num_views = models.IntegerField()
    is_done = models.BooleanField()



