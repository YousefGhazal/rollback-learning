from django.http import JsonResponse
from .models import Book, Author
from django.db.models import F, Count, Sum, OuterRef, Subquery

# Create your views here.


def summary_view(request):
    # 1.Number of Books
    books_count = Book.objects.count()
    # 2.Number pages of all boods
    total_pages = Book.objects.aggregate(Sum("pages"))["pages__sum"]
    # 3.Number of Books for Author
    authors = Author.objects.annotate(books_count=Count("book"))
    # 4.Books pages > sold
    books = Book.objects.filter(pages__gt=F("sold"))
    # 5. Add 5 pages to all books
    Book.objects.update(pages=F("pages") + 5)
    updated_books = Book.objects.all()
    # 6. Books with Authors in one query
    books_with_authors = Book.objects.select_related("author")
    # 7. Authors with their books in one query
    authors_with_books = Author.objects.prefetch_related("book_set")
    # 8. Authors with total pages in their books
    author_with_total_pages = Author.objects.annotate(total_pages=Sum("book__pages"))

    data = {
        "number_of_books": books_count,
        "total_pages_in_books": total_pages,
        "authors_books_count": [
            {"author": author.name, "books_count": author.books_count}
            for author in authors
        ],
        "num_books": [
            {
                "title": book.title,
                "pages": book.pages,
                "sold": book.sold,
            }
            for book in books
        ],
        "add_pages": [
            {
                "pages": book.pages,
            }
            for book in updated_books
        ],
        "books_with_authors": [
            {"title": book.title, "author": book.author.name}
            for book in books_with_authors
        ],
        "author_with_books": [
            {
                "author": author.name,
                "book": [book.title for book in author.book_set.all()],
            }
            for author in authors_with_books
        ],
        "author_with_total_pages": [
            {"author": author.name, "total_pages": author.total_pages}
            for author in author_with_total_pages
        ],
    }

    return JsonResponse(data)


# Subquery example
latest_book_qs = Book.objects.filter(author=OuterRef("pk")).order_by("-created_at")
authors_with_latest_book = Author.objects.annotate(
    latest_book_title=Subquery(latest_book_qs.values("title")[:1])
)
print(authors_with_latest_book, "authors_with_latest_book")
