from django.db import models

from books.models import BookRead


class Memo(models.Model):
    title = models.CharField(max_length=64)
    context = models.TextField()
    book_read = models.ForeignKey(BookRead, on_delete=models.CASCADE)
