from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    isbn = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    summary = models.TextField()


class BookRead(models.Model):
    is_read = models.BooleanField()
    is_recommended = models.BooleanField()
    stars = models.IntegerField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
