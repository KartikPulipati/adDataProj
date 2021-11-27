from django.db import models
from rater.models import rater
from django.contrib.auth.models import User

class business(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=500, blank=False)
    company_website = models.URLField()
    email = models.EmailField()
    is_email_verified = models.BooleanField(default=False)
    credits = models.IntegerField(default=0)

    def __str__(self):
        return self.owner.company_name

MAX_TITLE_LENGTH = 200

class advertisement(models.Model):
    title = models.CharField(max_length=MAX_TITLE_LENGTH)
    media_file = models.FileField(upload_to='media/')
    uploader = models.OneToOneField(business, on_delete=models.PROTECT)
    # upload_date = models.DateField(auto_add_now=True)
    reward_per_question = models.FloatField()
    viewers = models.ManyToManyField(rater)
    num_views = models.IntegerField()
    is_done = models.BooleanField()










