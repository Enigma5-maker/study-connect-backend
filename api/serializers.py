from rest_framework import serializers
from .models import StudyGroup, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class StudyGroupSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    members_count = serializers.SerializerMethodField()

    class Meta:
        model = StudyGroup
        fields = ['id', 'name', 'description', 'author', 'category', 'max_slots', 'members_count']

    def get_members_count(self, obj):
        return obj.users.count()

    def validate(self, data):
        if 'max_slots' in data and data['max_slots'] > 6:
            raise serializers.ValidationError("В группе не может быть больше 6 человек!")
        return data