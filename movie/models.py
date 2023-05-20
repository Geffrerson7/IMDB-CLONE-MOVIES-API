from django.db import models
from user.models import User
from django.contrib.postgres.fields import ArrayField

class Movie(models.Model):

    adult = models.BooleanField(default=False)
    backdrop_path = models.CharField(max_length=255)
    genres = ArrayField(models.JSONField())
    homepage = models.CharField(max_length=255)
    imdb_id = models.CharField(max_length=255)
    movie_id = models.IntegerField(unique=True)
    original_language = models.CharField(max_length=10)
    original_title = models.CharField(max_length=255)
    overview = models.TextField()
    popularity = models.FloatField()
    poster_path = models.CharField(max_length=255)
    production_companies = ArrayField(models.JSONField())
    runtime = models.IntegerField()
    release_date = models.DateField()
    tagline = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255)
    video = models.BooleanField(default=False)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")

    class Meta:
        db_table = "Movie"

    def __str__(self):
        return f"{self.movie_id}"