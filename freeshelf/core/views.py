from django.shortcuts import render
from core.models import Book, Category
from django.views import generic


class BookListView(generic.ListView):
    model = Book

