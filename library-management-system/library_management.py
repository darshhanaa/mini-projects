import json
import os

FILE_NAME = "books.json"

# -------------------------------
# Load books from file
# -------------------------------
def load_books():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                books = json.load(file)
                print(f"\n{len(books)} book(s) loaded successfully.\n")
                return books
        except:
            print("\nError loading books. Starting with an empty library.\n")
            return []
    else:
        print("\nNo previous library found. Starting a new library.\n")
        return []


# -------------------------------
# Save books to file
# -------------------------------
def save_books():
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)


# -------------------------------
# Add Book
# -------------------------------
def add_book():
    print("\n----- Add Book -----")

    title = input("Enter title: ").strip()

    if title == "":
        print("Title cannot be empty.")
        return

    author = input("Enter author: ").strip()

    if author == "":
        print("Author cannot be empty.")
        return

    while True:
        year = input("Enter publication year: ").strip()

        if year.isdigit():
            year = int(year)
            break
        else:
            print("Please enter a valid year.")

    books.append({
        "title": title,
        "author": author,
        "year": year
    })

    save_books()
    print("Book added successfully!")


# -------------------------------
# View Books
# -------------------------------
def view_books():
    print("\n----- Library Books -----")

    if len(books) == 0:
        print("No books available.")
        return

    for i, book in enumerate(books, start=1):
        print("-" * 35)
        print(f"Book {i}")
        print("-" * 35)
        print(f"Title : {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Year  : {book['year']}")
    print("-" * 35)


# -------------------------------
# Search Book
# -------------------------------
def search_book():
    title = input("\nEnter title to search: ").strip().lower()

    found = False

    for book in books:
        if book["title"].lower() == title:
            print("\nBook Found")
            print("-" * 30)
            print(f"Title : {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Year  : {book['year']}")
            found = True
            break

    if not found:
        print("Book not found.")


# -------------------------------
# Update Book
# -------------------------------
def update_book():
    title = input("\nEnter book title to update: ").strip().lower()

    for book in books:
        if book["title"].lower() == title:

            print("\nLeave blank to keep old value.")

            new_title = input(f"New title ({book['title']}): ").strip()
            new_author = input(f"New author ({book['author']}): ").strip()
            new_year = input(f"New year ({book['year']}): ").strip()

            if new_title:
                book["title"] = new_title

            if new_author:
                book["author"] = new_author

            if new_year:
                if new_year.isdigit():
                    book["year"] = int(new_year)
                else:
                    print("Invalid year. Old year kept.")

            save_books()
            print("Book updated successfully!")
            return

    print("Book not found.")


# -------------------------------
# Delete Book
# -------------------------------
def delete_book():
    title = input("\nEnter title to delete: ").strip().lower()

    for book in books:
        if book["title"].lower() == title:
            books.remove(book)
            save_books()
            print("Book deleted successfully!")
            return

    print("Book not found.")


# -------------------------------
# Main Program
# -------------------------------
books = load_books()

while True:

    print("\n========== Library Management System ==========")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        update_book()

    elif choice == "5":
        delete_book()

    elif choice == "6":
        save_books()
        print("\nLibrary saved successfully.")
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
