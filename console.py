import pdb
from models.book import Book
from models.author import Author

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

book_repository.delete_all()
author_repository.delete_all()

author_1 = Author("J.K. Rowling")
author_repository.save(author_1)

book_1 = Book("Harry Potter 1", author_1)
book_repository.save(book_1)




pdb.set_trace()