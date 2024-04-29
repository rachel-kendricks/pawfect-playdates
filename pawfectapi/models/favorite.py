from django.db import models
from django.contrib.auth.models import User
from pawfectapi.models.pet import Pet


class Favorite(models.Model):
    user = models.ForeignKey(User, related_name="favorites", on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
