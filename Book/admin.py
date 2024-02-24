from django.contrib import admin
from Book.models import book, genre, loan

# Register your models here.
class genresAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_created',)
    search_fields = ('name',)

class booksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'edition', 'publishing_company', 'price_loan')
    search_fields = ('title',)

class loanAdmin(admin.ModelAdmin):
    list_display = ('name_user', 'name_book', 'loan_rate', 'loan_created_at')
    search_fields = ('name_user',)

admin.site.register(loan, loanAdmin)
admin.site.register(book, booksAdmin)
admin.site.register(genre, genresAdmin)