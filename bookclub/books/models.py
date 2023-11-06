from django.db import models

class Book(models.Model):
    book = models.CharField(max_length=50)
    description = models.TextField()
    author = models.CharField(max_length=50)
    release_date = models.DateField()
    genre = models.CharField(max_length=50)

class User(models.Model):
    username = models.CharField(max_length=15, blank=False)
    password = models.CharField(max_length=15, blank=False)
    email = models.EmailField(blank=False)
    birthday = models.DateField(blank=False)

class Club(models.Model):
    name = models.CharField(max_length=100, blank=False)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    description = models.TextField()
    members = models.ManyToManyField(User)

class Messages(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(blank=False)
    time = models.DateTimeField()

class Reviews(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    rating = models.PositiveIntegerField(default=0, max_length=5)
    time = models.DateTimeField





