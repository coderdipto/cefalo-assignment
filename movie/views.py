from rest_framework import viewsets
from rest_framework.response import Response

from movie.models import Movie
from movie.serializers import MovieSerializer, MovieSerializerFormattedInfo


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = Movie.objects.all()
        serializer = MovieSerializerFormattedInfo(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = MovieSerializerFormattedInfo(instance)
        return Response(serializer.data)
