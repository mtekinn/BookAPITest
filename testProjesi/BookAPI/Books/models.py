from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_data = models.DateField()
    isbn_number = models.CharField(max_length=13)
    page_count = models.IntegerField()
    cover_image = models.ImageField(upload_to='covers/', null=True, blank=True)
    language = models.CharField(max_length=20)

    def __str__(self):
        return self.title