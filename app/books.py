from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)
from flask_login import login_required

from .models import Book
from . import db

books = Blueprint("books", __name__)


@books.route("/books")
@login_required
def list_books():
    title = request.args.get("title", "")
    author = request.args.get("author", "")
    language = request.args.get("language", "")
    publication_year = request.args.get("publication_year", "")

    query = Book.query

    if title:
        query = query.filter(Book.title.ilike(f"%{title}%"))

    if author:
        query = query.filter(Book.author.ilike(f"%{author}%"))

    if language:
        query = query.filter(Book.language.ilike(f"%{language}%"))

    if publication_year:
        query = query.filter(Book.publication_year == publication_year)

    all_books = query.all()

    return render_template("books.html", books=all_books)


@books.route("/book/<int:id>")
@login_required
def book_details(id):
    book = Book.query.get_or_404(id)
    return render_template("book_details.html", book=book)


@books.route("/add_book", methods=["GET", "POST"])
@login_required
def add_book():
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        publication_year = request.form.get("publication_year")
        language = request.form.get("language")
        isbn = request.form.get("isbn")
        copies_total = request.form.get("copies_total")

        existing_book = Book.query.filter_by(isbn=isbn).first()

        if existing_book:
            flash("Book with this ISBN already exists.", "danger")
            return redirect(url_for("books.add_book"))

        new_book = Book(
            title=title,
            author=author,
            publication_year=int(publication_year) if publication_year else None,
            language=language,
            isbn=isbn,
            copies_total=int(copies_total),
            copies_available=int(copies_total)
        )

        db.session.add(new_book)
        db.session.commit()

        flash("Book added successfully!", "success")
        return redirect(url_for("books.list_books"))

    return render_template("add_book.html")


@books.route("/edit_book/<int:id>", methods=["GET", "POST"])
@login_required
def edit_book(id):
    book = Book.query.get_or_404(id)

    if request.method == "POST":
        book.title = request.form.get("title")
        book.author = request.form.get("author")
        publication_year = request.form.get("publication_year")
        book.publication_year = int(publication_year) if publication_year else None
        book.language = request.form.get("language")
        book.isbn = request.form.get("isbn")

        new_total = int(request.form.get("copies_total"))
        borrowed_books = book.copies_total - book.copies_available

        book.copies_total = new_total
        book.copies_available = max(new_total - borrowed_books, 0)

        db.session.commit()

        flash("Book updated successfully!", "success")
        return redirect(url_for("books.list_books"))

    return render_template("edit_book.html", book=book)


@books.route("/delete_book/<int:id>")
@login_required
def delete_book(id):
    book = Book.query.get_or_404(id)

    db.session.delete(book)
    db.session.commit()

    flash("Book deleted successfully!", "warning")
    return redirect(url_for("books.list_books"))