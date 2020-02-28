import os
import pandas as pd
from django.core.management import BaseCommand

from crawler.settings import BASE_DIR
from movie.models import Movie

movie_csv = os.path.join(BASE_DIR, 'movies.csv')
rating_csv = os.path.join(BASE_DIR, 'ratings.csv')


def name_without_the(title):
    if title.lower().startswith("the"):
        return title.lower().split("the", 1)[-1]
    return title


def find_rating(title, year):
    try:
        movie_df = pd.read_csv(movie_csv)
        filter1 = movie_df["title"].str.contains(title, case=False)
        filter2 = movie_df["title"].str.contains(year)
        row_count = movie_df[movie_df.where(filter1 & filter2).movieId.notnull()].shape[0]

        if row_count == 1:
            movie_id = movie_df[movie_df.where(filter1 & filter2).movieId.notnull()]['movieId'].values.item()
            rating_df = pd.read_csv(rating_csv)
            avg_rating = rating_df.loc[rating_df['movieId'].isin([int(movie_id)])]['rating'].mean()
            rating_count = rating_df.loc[rating_df['movieId'].isin([int(movie_id)])]['rating'].shape[0]
            return avg_rating, rating_count
    except Exception as e:
        print(str(e))
        pass

    return None, None


class Command(BaseCommand):
    def handle(self, *args, **options):
        movies = Movie.objects.all()
        for movie in movies:
            avg_rating, rating_givers = find_rating(name_without_the(movie.title), movie.year)

            if avg_rating and rating_givers:
                movie.average_rating = avg_rating
                movie.rating_givers = rating_givers
                movie.save()
                print("Updated Movie {} with average rating: {} and rating giver: {}".format(movie.title, avg_rating,
                                                                                             rating_givers))
