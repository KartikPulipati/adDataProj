from django.db import models
from rater.models import rater
from django.contrib.auth.models import User

class business(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=500, blank=False)
    company_website = models.URLField()
    is_email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.owner.company_name

MAX_TITLE_LENGTH = 200
MAX_QUESTION_LENGTH = 500
MAX_ANSWER_LENGTH = 1000

class advertisement(models.Model):
    title = models.CharField(max_length=MAX_TITLE_LENGTH)
    media_file = models.FileField(upload_to='adverMedia/%Y/%m/%d/')
    uploader = models.ForeignKey(business, on_delete=models.CASCADE)
    reward_per_question = models.FloatField()
    viewers = models.ManyToManyField(rater, on_delete=models.PROTECT)
    num_views = models.IntegerField()
    is_done = models.BooleanField()

class Question(models.Model):
    advertisement = models.ForeignKey(advertisement, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=MAX_QUESTION_LENGTH)
    answer_text = models.CharField(max_length=MAX_ANSWER_LENGTH)










