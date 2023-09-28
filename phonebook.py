
people = {
    "carter": "+254707035002",
    "david": "+25470701655556",
}
name = input("Name: ")
if name in people:
    number = people[name]
    print(f"Number: {number}")


import csv
with open("phonebook.csv","a") as file:
    name = input("Name: ")
    number = input("Number: ")
    writer = csv.writer(file)
    writer.writerow([name, number])
#### BETTER METHOD
with open("phonebook.csv","a") as file:
    name = input("Name: ")
    number = input("Number: ")
    writer = csv.DictWriter(file, fieldnames={["name", "number"]})
    writer.writerow({"name": name, "number":number})
