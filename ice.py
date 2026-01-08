library = []

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    library.append({
        "id": book_id,
        "title": title,
        "author": author,
        "issued": False
    })
    print("Book added successfully.")

def view_books():
    if not library:
        print("No books available.")
        return
    print("\nAvailable Books:")
    for book in library:
        status = "Issued" if book["issued"] else "Available"
        print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Status: {status}")

def issue_book():
    book_id = input("Enter Book ID to issue: ")
    for book in library:
        if book["id"] == book_id:
            if book["issued"]:
                print("Book already issued.")
            else:
                book["issued"] = True
                print("Book issued successfully.")
            return
    print("Book not found.")

def return_book():
    book_id = input("Enter Book ID to return: ")
    for book in library:
        if book["id"] == book_id:
            if not book["issued"]:
                print("Book was not issued.")
            else:
                book["issued"] = False
                print("Book returned successfully.")
            return
    print("Book not found.")

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        print("Exiting Library System.")
        break
    else:
        print("Invalid choice.")