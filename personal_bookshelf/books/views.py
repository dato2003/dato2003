from django.views.generic import ListView , CreateView, DetailView, UpdateView,DeleteView
from django.shortcuts import render,redirect,get_object_or_404
from .models import author,book
from .forms import bookforms, authorforms
from django.urls import reverse_lazy

class BookListView(ListView):
    model= book
    tenplate_name = "books/book_list.html"
    context_object_name = "books"


class BookDetailView(DetailView):
    model= book
    template_name = 'books/book_detail.html'

class BookCreateView(CreateView):
    model=book
    form_class = bookforms
    template_name = 'books/book_edit.html'
    success_url = reverse_lazy("book_list")

class BookUpdateView(UpdateView):
    model=book
    form_class= bookforms
    template_name = 'books/book_edit.html'
    success_url = reverse_lazy("book_list")
    

class BookDeleteView(DeleteView):
    model = book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')

class AuthorListView(ListView):
    model= author
    template_name = "author/author.list.html"
    context_object_name = "authors"




class AuthorDetailView(DetailView):
    model= author
    template_name = "author/author.detail.html"

class AuthorCreateView(CreateView):
    model=author
    form_class = authorforms
    template_name = "author/author.edit.html"
    success_url = reverse_lazy("author.list")

class AuthorUpdateView(UpdateView):
    model=author
    form_class= authorforms
    template_name = "author/author.edit.html"
    success_url = reverse_lazy("author.list")    

class AuthorDeleteView(DeleteView):
    model = author
    template_name = "author/author.confirm.delete.html"
    success_url = reverse_lazy('author.list')