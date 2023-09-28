import csv
books =[]
# add books to your shelf by reading from book.csv
with open("book.csv")as file:
    file_reader = csv.DictReader(file)
    for book in file_reader:
        books.appened(book)

for book in books:
    print(book["title"])
print(books)