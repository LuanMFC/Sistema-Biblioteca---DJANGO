from django.contrib import admin
from Loan.models import loan

# Register your models here.
class loanAdmin(admin.ModelAdmin):
    list_display = ('name_user', 'name_book', 'loan_rate', 'loan_created_at')
    search_fields = ('name_user',)

admin.site.register(loan, loanAdmin)