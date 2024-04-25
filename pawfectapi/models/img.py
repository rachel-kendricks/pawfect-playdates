from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    img = models.URLField()
