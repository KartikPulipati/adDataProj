from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Business)
admin.site.register(models.Video)
admin.site.register(models.Tag)
