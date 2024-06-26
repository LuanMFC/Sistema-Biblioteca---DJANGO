"""
URL configuration for App project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from Book.views import book_ListView, book_CreateView, book_DetailView, book_UpdateView, book_DeleteView
from Loan.views import LoanCreateView, LoanListView
from Account.views import Login, Register, Logout
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', Login, name="login"),
    path('register/', Register, name="register"),
    path('logout/', Logout, name="logout"),
    path('list/', book_ListView.as_view(), name='list'),
    path('create_book/', book_CreateView.as_view(), name='create_book'),
    path('list/<int:pk>/', book_DetailView.as_view(), name='details_book'),
    path('list/<int:pk>/update', book_UpdateView.as_view(), name='update_book'),
    path('list/<int:pk>/delete/', book_DeleteView.as_view(), name='delete_book'),
    path('loan/', LoanCreateView.as_view(), name='loan_book'),
    path('list_loan/', LoanListView.as_view(), name='loanlist_book'),
    path('',book_ListView.as_view(), name='list')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
