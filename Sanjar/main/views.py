from rest_framework import viewsets, filters
from .models import StudyGroup, Category
from .serializers import StudyGroupSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class StudyGroupViewSet(viewsets.ModelViewSet):
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['category__id'] 

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)