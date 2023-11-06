from django.db import models

# bookclub/models.py


class Book(models.Model):
    book = models.CharField(max_length=50)
    description = models.TextField()
    author = models.CharField
    release_date = models.DateField
    genre = models.CharField



