text = "In the great green room"
words = text.split()
# round 1
print("round 1")
for word in words:
    print(word)
#round 2
print("round 2")
for word in words:
    for c in word:
        print(c)

#round 3
print("round 3")
for word in words:
    if "g" in word:
        print(word)
#round 4
print("round 4")
for word in words[2:]:
    print(word)
#round 5
print("round 5")
for word in words:
    print("Goodnight Moon")

