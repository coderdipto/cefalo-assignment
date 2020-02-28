from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    year = models.CharField(max_length=10, db_index=True)
    awards = models.CharField(max_length=10)
    nominations = models.CharField(max_length=10)
    average_rating = models.FloatField(null=True, blank=True)
    rating_givers = models.IntegerField(null=True, blank=True)
    info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = [['title', 'year']]
