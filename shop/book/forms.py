from django.forms import ModelForm
from models import Book, CommentBook


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'text', 'image', 'authors', 'publisher', 'cath', 'tags', 'langs', 'unit', 'price']


class CommentForm(ModelForm):
    class Meta:
        model = CommentBook
        fields = ['text']


