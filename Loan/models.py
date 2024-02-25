from django.db import models
from Book.models import book
from django.contrib.auth.models import User

class loan(models.Model):
    name_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_loans', null=True)
    name_book = models.ForeignKey(book, on_delete=models.PROTECT, related_name='book_loans')
    loan_rate = models.FloatField(null=True)
    loan_created_at = models.DateTimeField(auto_now_add=True)

    def Meta(self):
        ordering = ['-loan_created_at']

    def __self__(self):
        return f'{self.name_user} - {self.name_book}'
