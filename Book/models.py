from django.db import models
# Create your models here.

class genre(models.Model):
    name = models.CharField(max_length=200, null=False)
    date_created = models.DateField(null=False)

    def __str__(self):
        return self.name
    
class book(models.Model):
    title = models.CharField(max_length=200, null=False)
    author = models.CharField(max_length=200, null=False)
    genre = models.ForeignKey(genre, on_delete=models.PROTECT, related_name='books_genre')
    publishing_company = models.CharField(max_length=200, null=False)
    edition = models.CharField(max_length=50, null=False)
    photo = models.ImageField(upload_to="static/media")
    price_loan = models.FloatField(null=False)
    date_published = models.DateField(null=False)

    def __str__(self):
        return f'{self.title} - {self.edition}'