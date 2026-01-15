from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class StudyGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_groups')
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Membership', related_name='study_groups')
    max_members = models.PositiveIntegerField(default=6)

    def __str__(self):
        return self.name

class Membership(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)
