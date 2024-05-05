# first_num = int(input("enter first number:"))
# secont_num = int(input("enter second number:"))

# print(first_num+secont_num)

# a = int(input("enter first number:"))

# a = a*a
# print (a)

# a = int(input("enter number of kilometers to convert into miles"))
# a = a*0.6
# print(a,"miles")

# b = int(input("Breath of triangle"))
# h = int(input("Enterheight of triangle"))
# area = 0.5*b*h
# print("area of triangle is: ", area)


# Define a list of dictionaries representing books
books = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "format": "Paperback", "pages": 336, "available": True},
    {"title": "1984", "author": "George Orwell", "format": "Hardcover", "pages": 328, "available": False},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "format": "Paperback", "pages": 180, "available": True}
]

# Function to display information about books
def display_books(books):
    for book in books:
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Format: {book['format']}")
        print(f"Pages: {book['pages']}")
        print(f"Available: {'Yes' if book['available'] else 'No'}")
        print()

# Display the books
display_books(books)


