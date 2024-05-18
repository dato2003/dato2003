from django.urls import path
from .views import (BookCreateView,BookDeleteView,BookDetailView,BookListView,BookUpdateView,
AuthorCreateView,AuthorDeleteView,AuthorDetailView,AuthorUpdateView,AuthorListView)

urlpatterns =[

    path("book/<int:pk>/",BookDetailView.as_view(),name= "book_detail"),
    path("book/<int:pk>/edit/",BookUpdateView.as_view(),name= "edit_book"),
    path("book/new/",BookCreateView.as_view(),name= "new book"),
    path("book/list/",BookListView.as_view(),name = "book_list"),
    path("book/<int:pk>/delete",BookDeleteView.as_view(),name = "Book_delete"),
    path("author/<int:pk>/",AuthorDetailView.as_view(),name= "author.detail"),
    path("author/new/",AuthorCreateView.as_view(),name= "new author"),
    path("author/<int:pk>/delete/",AuthorDeleteView.as_view(),name="delete author"),
    path("author/<int:pk>/edit",AuthorUpdateView.as_view(),name="edit author"),
    path("author/list",AuthorListView.as_view(),name="author.list")
]