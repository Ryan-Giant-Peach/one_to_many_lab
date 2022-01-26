import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository


author1 = Author("Roald", "Dahl")
author_repository.save(author1)
author2 = Author("Roddy", "Doyle")
author_repository.save(author2)
author3 = Author("J.R.R", "Tolkein")
author_repository.save(author3)
author4 = Author("Ryan", "Caulfield")
author_repository.save(author4)

book1 = Book("The Twits", 100, author1)
book_repository.save(book1)
book2 = Book("The Giggler Treatment", 75, author2)
book_repository.save(book2)
book3 = Book("Lord of the Rings", 750000, author3)
book_repository.save(book3)
book4 = Book("How To Be Ryan", 10000000, author4)
book_repository.save(book4)

# book_repository.delete_all()
# author_repository.delete_all()

# author_repository.select_all()
# book_repository.select_all()

# task_1 = Task("Plant seeds", user1, 30)
# task_repository.save(task_1)

# task_2 = Task("Go for a run", user1, 30, True)
# task_repository.save(task_2)


pdb.set_trace()