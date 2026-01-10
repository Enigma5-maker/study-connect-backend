from django.db import models
from django.contrib.auth.models import User

# 1. Категории (Математика, Дизайн и т.д.)
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): return self.name

# 2. Группы обучения
class StudyGroup(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_groups')
    members = models.ManyToManyField(User, through='Membership', related_name='study_groups')
    max_members = models.PositiveIntegerField(default=6) # Тот самый лимит!

    def __str__(self): return self.name

# 3. Связь пользователей с группами
class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)
