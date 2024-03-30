
# Sharpen your skills in managing and modifying data within tuples and lists.

# Problem Statement:
# You are maintaining a library system where each book is stored as a tuple within a list. 
# Your task is to update this system by adding new books and ensuring no duplicates.

# Existing Library Data:

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# Add functionality to insert new books into library.
# Ensure that adding a duplicate book is handled appropriately.

def add_book(book_list):
    book_to_add = input("What is the title of the book you want to add?\n")
    for book in book_list:
        if book_to_add == book[0]:
            print("Book already in  library.")
            return book_list
    author = input("Who is the book's author?\n")
    book_list.append((book_to_add, author))
    return book_list

library = add_book(library)

def print_library(book_library):
    for book in book_library:
        print(f"Author: {book[1]}\nBook: {book[0]}")

print_library(library)