from flask import Blueprint, request
from .models import Book
from . import db

books = Blueprint("books", __name__)


@books.route("/add_book", methods=["GET", "POST"])
def add_book():

    if request.method == "POST":

        title = request.form.get("title")
        author = request.form.get("author")
        publication_year = request.form.get("publication_year")
        language = request.form.get("language")
        isbn = request.form.get("isbn")
        copies_total = request.form.get("copies_total")

        new_book = Book(
            title=title,
            author=author,
            publication_year=publication_year,
            language=language,
            isbn=isbn,
            copies_total=copies_total,
            copies_available=copies_total
        )

        db.session.add(new_book)
        db.session.commit()

        return "Book added successfully!"

    return """
    <h2>Add Book</h2>

    <form method="POST">

        Title:
        <input type="text" name="title"><br><br>

        Author:
        <input type="text" name="author"><br><br>

        Publication Year:
        <input type="number" name="publication_year"><br><br>

        Language:
        <input type="text" name="language"><br><br>

        ISBN:
        <input type="text" name="isbn"><br><br>

        Copies:
        <input type="number" name="copies_total"><br><br>

        <button type="submit">Add Book</button>

    </form>
    """


@books.route("/search")
def search_books():

    title = request.args.get("title")

    if title:
        books_found = Book.query.filter(
            Book.title.contains(title)
        ).all()

        result = ""

        for book in books_found:
            result += f"<p>{book.title} - {book.author}</p>"

        return result

    return """
    <h2>Search Books</h2>

    <form method="GET">

        Book Title:
        <input type="text" name="title">

        <button type="submit">Search</button>

    </form>
    """


@books.route("/edit_book/<int:id>", methods=["GET", "POST"])
def edit_book(id):

    book = Book.query.get_or_404(id)

    if request.method == "POST":

        book.title = request.form.get("title")
        book.author = request.form.get("author")

        db.session.commit()

        return "Book updated successfully!"

    return f'''
    <h2>Edit Book</h2>

    <form method="POST">

        Title:
        <input type="text" name="title" value="{book.title}"><br><br>

        Author:
        <input type="text" name="author" value="{book.author}"><br><br>

        <button type="submit">Update Book</button>

    </form>
    '''