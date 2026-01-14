from django.contrib import admin
from .models import Category, StudyGroup, Membership

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(StudyGroup)
class StudyGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'author', 'max_slots']

admin.site.register(Membership)