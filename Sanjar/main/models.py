from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    def _str_(self): return self.name

class StudyGroup(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_groups')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, through='Membership', related_name='study_groups')
    max_slots = models.PositiveIntegerField(default=6)

class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)