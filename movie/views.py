from rest_framework import viewsets
from .models import Movie
from .serializer import MovieSerializer
from rest_framework.permissions import IsAuthenticated
from .pagination import StandardResultsSetPagination


class MovieViewSet(viewsets.ModelViewSet):

    queryset = Movie.objects.all().order_by("id")
    serializer_class = MovieSerializer
    permission_classes =[IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user.id)