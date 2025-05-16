# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.



# # # Class method wo method hoti hai jo class ko directly affect karti hai, na ki instance ko.

# # # Class variable ko update karne ke liye cls use hota hai.

class Book():
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Books add karte hain
Book.increment_book_count()  # First book added
print(Book.total_books)  # Output: 1

Book.increment_book_count()  # Second book added
print(Book.total_books)  # Output: 2


