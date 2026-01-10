from rest_framework import viewsets
from .models import StudyGroup
from .serializers import GroupSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset =StudyGroup.objects.all()
    serializer_class =GroupSerializer
