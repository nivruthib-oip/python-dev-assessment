class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def get_age(self):
        return 2025 - self.publication_year

    def get_summary(self):
        return "Title: " + self.title + ", Author: " + self.author + ", Published: " + str(self.publication_year)


# Create Book objects
book1 = Book("Harry Potter", "J.K. Rowling", "1234567890", 1997)
book2 = Book("The Alchemist", "Paulo Coelho", "0987654321", 1988)


print("Book 1")
print("Title:", book1.title)
print("Author:", book1.author)
print("Age:", book1.get_age())
print("Summary:", book1.get_summary())

print("\nBook 2")
print("Title:", book2.title)
print("Author:", book2.author)
print("Age:", book2.get_age())
print("Summary:", book2.get_summary())