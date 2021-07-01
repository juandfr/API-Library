from django.contrib import admin
from .models import Books
from django import forms

admin.site.register(Books)


class Book(admin.ModelAdmin):
    list_display = ('id_book', 'title')
    list_display_link = ('id_book', 'title')
    search_fields = ('title')