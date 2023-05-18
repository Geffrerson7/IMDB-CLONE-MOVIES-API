from .models import Movie
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            "id",
            "adult",
            "genres",
            "homepage",
            "imdb_id",
            "movie_id",
            "original_language",
            "original_title",
            "overview",
            "popularity",
            "poster_path",
            "production_companies",
            "runtime",
            "release_date",
            "tagline",
            "title",
            "video",
            "vote_average",
            "vote_count",
       )