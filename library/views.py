from django.views import generic
from .models import Author, Book


class IndexView(generic.ListView):
    template_name = 'library/index.html'
    context_object_name = 'all_books'

    def get_queryset(self):
        return Book.objects.order_by('pub_date')


class AuthorView(generic.DetailView):
    model = Author
    template_name = 'library/author.html'


