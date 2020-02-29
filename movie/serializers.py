import json
from rest_framework import serializers

from movie.models import Movie


class MovieSerializerFormattedInfo(serializers.ModelSerializer):
    info = serializers.SerializerMethodField()

    def get_info(self, obj):
        return json.loads(obj.info)

    class Meta:
        model = Movie
        fields = ('title', 'year', 'awards', 'nominations', 'average_rating', 'rating_givers', 'info')


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'year', 'awards', 'nominations', 'average_rating', 'rating_givers', 'info')
