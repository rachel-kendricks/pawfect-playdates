from django.db import models
from django.contrib.auth.models import User


class Size(models.Model):
    name = models.CharField(max_length=255)
