from django.db import models
from rater.models import rater
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class business(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=500, blank=False)
    company_website = models.URLField()
    is_email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.owner.company_name

MAX_TITLE_LENGTH = 200


class advertisement(models.Model):
    title = models.CharField(max_length=MAX_TITLE_LENGTH)
    media_file = models.FileField(upload_to='adverMedia/%Y/%m/%d/')
    uploader = models.ForeignKey(business, on_delete=models.CASCADE)
    reward = models.PositiveIntegerField(blank=False)
    viewers = models.ManyToManyField(rater, blank=False)
    num_views = models.IntegerField(default=0)
    is_done = models.BooleanField(default=False)

class answer(models.Model):
    user = models.ForeignKey(rater, related_name='answered', on_delete=models.PROTECT)
    ad = models.ForeignKey(advertisement, related_name='answers', on_delete=models.CASCADE)
    opinion = models.TextField(max_length=6000)
    rating = models.IntegerField(blank=False, validators=[MaxValueValidator(5), MinValueValidator(1)])

    def __str__(self):
        return f'{self.advertisement.title} - {self.rater.user.first_name}'












