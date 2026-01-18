import time
import mysql.connector
from difflib import get_close_matches


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="home@123",
        database="mydb"
    )


class Books:
    def __init__(self, book_id, name, author, available_for_booking=True):
        self.id = book_id
        self.name = name
        self.author = author
        self.available_for_booking = available_for_booking


class Users:
    def __init__(self, user_name, user_id):
        self.user_name = user_name
        self.user_id = user_id
        self.books_borrowed = []

    @staticmethod
    def load_books_from_db():
        """Fetches all books from the SQL database."""
        books_list = []
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT id, title, author, available FROM books")
        for row in cursor.fetchall():
            books_list.append(Books(row['id'], row['title'], row['author'], bool(row['available'])))
        conn.close()
        return books_list

    @staticmethod
    def view_available_books_formatted(books):
        print("-" * 85)
        print(f"{'ID':<5} {'Book Name':<50} {'Author'}")
        print("-" * 85)
        count = 0
        for book in books:
            if book.available_for_booking:
                print(f"{book.id:<5} {book.name:<50} {book.author}")
                count += 1
        print("-" * 85)
        print(f"Total Available Books: {count}\n")

    def update_db_status(self, book_id, status):
        """Updates the 'available' column in SQL."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE books SET available = %s WHERE id = %s", (status, book_id))
        conn.commit()
        conn.close()

    def borrow_book(self, book):
        if book.available_for_booking:
            self.books_borrowed.append(book.name)
            book.available_for_booking = False
            self.update_db_status(book.id, False)  # Sync with SQL
            return f"{self.user_name} has borrowed '{book.name}'"
        return f"Sorry, '{book.name}' is not available"

    def return_book(self, book):
        if book.name in self.books_borrowed:
            self.books_borrowed.remove(book.name)
            book.available_for_booking = True
            self.update_db_status(book.id, True)  # Sync with SQL
            return f"{self.user_name} has returned '{book.name}'"
        return f"{self.user_name} did not borrow '{book.name}'"

    def user_info(self):
        return f"User Name: {self.user_name}, User ID: {self.user_id}"

    @staticmethod
    def search_books_by_author(books, author_name, cutoff=0.7):
        matched_books = []
        for book in books:
            if get_close_matches(author_name.lower(), [book.author.lower()], cutoff=cutoff):
                matched_books.append(book.name)
        return f"Books by {author_name}: {', '.join(matched_books)}" if matched_books else "No books found"


# --- MAIN SYSTEM ---

# Initial load from Database
all_books = Users.load_books_from_db()
user = Users("Vijay", "U001")


def display_menu():
    print("\n**** LIBRARY MANAGEMENT SYSTEM (SQL CONNECTED) ****")
    print("1. View Available Books")
    print("2. Borrow a Book (Enter ID)")
    print("3. Return a Book (Enter ID)")
    print("4. View Borrowed Books")
    print("5. User Information")
    print("6. Search Book by Author")
    print("7. Exit")


while True:
    display_menu()
    choice = input("Enter your choice (1-7): ").strip()

    if choice == '1':
        Users.view_available_books_formatted(all_books)

    elif choice == '2':
        try:
            bid = int(input("Enter the Book ID to borrow: "))
            book_to_borrow = next((b for b in all_books if b.id == bid), None)
            if book_to_borrow:
                print(user.borrow_book(book_to_borrow))
            else:
                print("Invalid Book ID.")
        except ValueError:
            print("Please enter a numeric ID.")

    elif choice == '3':
        try:
            bid = int(input("Enter the Book ID to return: "))
            book_to_return = next((b for b in all_books if b.id == bid), None)
            if book_to_return:
                print(user.return_book(book_to_return))
            else:
                print("Invalid Book ID.")
        except ValueError:
            print("Please enter a numeric ID.")

    elif choice == '4':
        print(f"{user.user_name} has borrowed: {', '.join(user.books_borrowed) if user.books_borrowed else 'No books'}")

    elif choice == '5':
        print(user.user_info())

    elif choice == '6':
        author_name = input("Enter author name: ").strip()
        print(Users.search_books_by_author(all_books, author_name))

    elif choice == '7':
        print("Goodbye!")
        break

    time.sleep(1)