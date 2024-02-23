from django.db import models
from django.contrib.auth.models import User

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
    
class loan(models.Model):
    name_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_loans')
    name_book = models.ForeignKey(book, on_delete=models.PROTECT, related_name='book_loans')
    loan_rate = models.FloatField(null=False)
    loan_created_at = models.DateTimeField(auto_now_add=True)

    def Meta(self):
        ordering = ['-loan_created_at']

    def __self__(self):
        return f'{self.name_user} - {self.name_book}'