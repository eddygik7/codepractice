from cs50 import SQL
db = SQL("sqlite:///favorites.db")
favorite = input("favorite: ")
rows = db.execute("select count(*) as n from favorites where problem =?",favorite)

print(rows[0]["n"])
