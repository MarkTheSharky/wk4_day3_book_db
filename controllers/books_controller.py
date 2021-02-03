from flask import Flask, render_template, redirect, request, Blueprint
from repositories import author_repository, book_repository

from models.book import Book
from models.author import Author

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books = books)

@books_blueprint.route("/books/<id>/delete", methods=["POST"])
def delete_book(id):
    book_repository.delete(id)
    return redirect("/books")

@books_blueprint.route("/books/new")
def new_book():
    books = book_repository.select_all()
    return render_template("books/new.html", all_books=books)   

@books_blueprint.route("/books", methods=["POST"])
def create_book():
    book_list = book_repository.select_all()
    for book in book_list:
        if book.author.name == request.form["author"]:
            new_book = Book(request.form["title"], book.author)
            book_repository.save(new_book)
            return
        else:
            new_author = Author(request.form["author"])
            author_repository.save(new_author)
            new_book = Book(request.form["title"], new_author)
            book_repository.save(new_book)
            

    return redirect("/books")
