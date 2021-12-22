from django.contrib.auth.models import User
from django.db import models
from datetime import date


class rater(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(blank=False)

    def cal_age(self):
        today = date.today()
        return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))

    genders = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=6, choices=genders, blank=False)
    is_email_verified = models.BooleanField(default=False)
    credits = models.IntegerField(default=0)

    class Meta:
        pass

    def __str__(self):
        return self.user.username


