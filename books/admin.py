from django.contrib import admin
from .models import Books
from django import forms

admin.site.register(Books)

class AuthorAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'

