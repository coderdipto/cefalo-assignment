import json
from rest_framework import serializers

from movie.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'year', 'awards', 'nominations', 'average_rating', 'rating_givers', 'info')
