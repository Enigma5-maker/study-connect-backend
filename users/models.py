from django.db import models
from django.contrib.auth.models import (AbstractUser)


class Studyuser(AbstractUser):
    username = models.CharField(max_length=155, unique=True)
    email = models.EmailField()