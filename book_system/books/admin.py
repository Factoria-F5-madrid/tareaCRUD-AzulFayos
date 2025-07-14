from django.contrib import admin
from .models import Book

@admin.register(Book)
class LibroAdmin(admin.ModelAdmin):
  list_display = ('title', 'autor', 'publication_date', 'isbn')
  search_fields = ('title', 'autor', 'isbn')
  list_filter = ('publication_date',)