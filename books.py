books = []
x = int(input("how many books: "))
for i in range(x):
    book=dict()
    book["title"] = input("title: ").strip().capitalize()
    book["author"]=input("Author: ")
    books.append(book)
for book in books:
    print(book["title"])
print(books)