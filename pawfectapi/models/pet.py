from django.db import models
from django.contrib.auth.models import User  # type: ignore
from pawfectapi.models.play_style import Play_style
from pawfectapi.models.size import Size


class Pet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    play_style = models.ForeignKey(Play_style, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255)
