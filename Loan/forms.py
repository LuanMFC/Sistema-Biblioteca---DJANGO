from django import forms
from Loan.models import loan


class LoanForm(forms.ModelForm):

    class Meta:
        model = loan
        fields = ('__all__')
        exclude = ['name_user']