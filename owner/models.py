from django.db import models
from rater.models import rater

MAX_TITLE_LENGTH = 200

class Advertisement(models.Model):
    title = models.CharField(max_length=MAX_TITLE_LENGTH)
    media_file = models.FileField(upload_to='media/')
    uploader = models.OneToOneField(Business, on_delete=models.CASCADE)
    upload_date = models.DateField(auto_add_now=True)
    viewers = models.ManyToManyField(rater)
    num_views = models.IntegerField()
    reward_per_question = models.FloatField()
    max_num_responses = models.IntegerField()
    is_done = models.BooleanField()



