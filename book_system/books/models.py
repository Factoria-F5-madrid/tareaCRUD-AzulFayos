from django.db import models

class Book(models.Model):
  title = models.CharField(max_length=200)
  autor = models.CharField(max_length=100)
  description = models.TextField()
  publication_date = models.DateField()
  isbn = models.CharField(max_length=13, unique=True)

  def __str__(self):
    return self.title