from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from Book.forms import BookForm
from Book.models import book


# Create your views here.
class book_ListView(ListView):
    model = book
    template_name = 'book_list.html'
    context_object_name = 'listBook'

    def get_queryset(self):
        listBook = super().get_queryset().order_by('title')
        searchBook = self.request.GET.get('search')

        if searchBook:
            listBook = super().get_queryset().filter(title__icontains=searchBook)
        return listBook
    
class book_CreateView(CreateView):
    model = book
    form_class = BookForm
    template_name = 'book_create.html'
    success_url = '/list'

class book_DetailView(DetailView):
    model = book
    template_name = 'book_details.html'

class book_UpdateView(UpdateView):
    model = book
    form_class = BookForm
    template_name = 'book_update.html'
    success_url = '/list'

class book_DeleteView(DeleteView):
    model = book
    success_url = '/list'

