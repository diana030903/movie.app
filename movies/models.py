from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    release_year = models.IntegerField()
    photo = models.ImageField(upload_to='photos/')
    plot = models.TextField()
    watch_date = models.DateField()
    rating = models.FloatField()

    def __str__(self):
        return self.title
