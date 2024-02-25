from Loan.forms import LoanForm
from Loan.models import loan
from django.views.generic import CreateView, ListView

# Create your views here.
class LoanCreateView(CreateView):
    model = loan
    template_name = 'loan_create.html'
    form_class = LoanForm
    success_url = '/list'
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.name_user_id = self.request.user.pk
        return super().form_valid(form)

class LoanListView(ListView):
    model = loan
    template_name = 'loan_list.html'
    context_object_name = 'loan'

    def get_queryset(self):
        # Carrega todos os objetos de Loan, juntamente com os objetos relacionados de Book
        return loan.objects.prefetch_related('name_book').all()